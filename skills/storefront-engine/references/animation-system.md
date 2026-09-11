# Managed Motion  -  Storefront Agent Reference

House motion requirements are defined in `references/design-rules.md` N10.
Choose at most the plan-named moment or a response to a shopper action;
this reference owns the managed runtime APIs, not another motion budget.

Lexsis supports open-ended custom animation without requiring a named scene or
a custom island for every visual idea. Agents author the composition; the MCP
compiler and renderer own capability validation, resource loading, lifecycle,
cleanup, reduced motion, and performance limits.

## Choose the lightest valid approach

| Need | Use |
|---|---|
| Hover or focus feedback | CSS color or border transition |
| The approved single motion moment | A managed module with explicit capabilities |
| Custom timeline or interaction | Managed motion with WAAPI or GSAP |
| Procedural drawing | Managed Canvas 2D |
| Custom shaders | Managed WebGL |
| Interactive 3D product or environment | Managed Three.js |
| Supplied vector/state-machine animation | Managed Lottie or Rive |
| Reusable stateful commerce/UI behavior | An island |

Do not create an island solely to hold a one-off timeline, shader, particle
field, 3D object, or scroll composition.

## Source contract

Place the motion block in the same source section as its markup:

```html
<!-- section: product-hero-object -->
<section id="product-hero-object" class="product-object">
  <canvas class="product-canvas" aria-label="Interactive product view"></canvas>
  <img
    class="product-fallback"
    src="https://cdn.example.com/product-static.webp"
    alt="Product front view"
  >
</section>

<script
  type="application/lexsis-motion"
  data-motion-id="product-hero-object"
  data-capabilities="three resize"
  data-mode="interaction"
  data-importance="decorative"
  data-reduced-motion="static"
>
async ({ dom, three, resize, scheduler, quality }) => {
  // Agent-authored motion.
}
</script>
```

The script body must be one function expression. The MCP compiler extracts it
into `section.motion[]`; never hand-write that compiled representation.

### Module attributes

| Attribute | Values | Meaning |
|---|---|---|
| `data-motion-id` | Unique identifier | Runtime diagnostics and source round-trip |
| `data-capabilities` | Space/comma-separated capabilities | APIs granted to the module |
| `data-mode` | `entrance`, `interaction`, `scroll`, `continuous` | Execution pattern |
| `data-importance` | `essential`, `decorative` | Whether motion carries required meaning |
| `data-reduced-motion` | `static`, `simplified` | Reduced-motion behavior |

Defaults are `entrance`, `decorative`, and `static`. Capabilities are never
inferred as permission: declare every capability the code uses.

## Runtime APIs

Always available:

- `root`
- `dom.query()`, `dom.queryAll()`, `dom.on()`, `dom.create()`, `dom.append()`
- `scheduler.frame()`, `scheduler.loop()`, `scheduler.timeout()`,
  `scheduler.interval()`, `scheduler.addCleanup()`
- `quality.tier`, `quality.dpr`, `quality.fps`
- `preferences.reducedMotion`, `saveData`, `colorScheme`, `contrast`
- `assets.url()`, `assets.json()`, `assets.image()`

Declared capabilities:

| Capability | Runtime API |
|---|---|
| `waapi` | `waapi.animate()` |
| `svg` | `svg.create()`, `svg.set()` |
| `gsap` | `gsap.load()`, `gsap.withContext()` |
| `scroll` | `scroll.on()`, `scroll.progress()` |
| `pointer` | `pointer.onMove()`, `onEnter()`, `onLeave()` |
| `resize` | `resize.observe()` |
| `visibility` | `visibility.observe()` |
| `canvas` | `canvas.context2d()`, `canvas.fit()` |
| `webgl` | `webgl.context()` |
| `three` | `three.load()` |
| `lottie` | `assets.lottie.mount()` |
| `rive` | `assets.rive.mount()` |
| `video` | `media.source()` |
| `events` | `events.on()`, `events.emit()` |

Undeclared capability APIs are removed from the runtime context.

## Scroll reveal with WAAPI

Content stays visible by default. The running animation supplies the temporary
starting state, preventing a failed module from leaving a blank section.

```html
<script
  type="application/lexsis-motion"
  data-motion-id="material-reveal"
  data-capabilities="visibility waapi"
  data-mode="scroll"
  data-reduced-motion="static"
>
({ dom, visibility, waapi }) => {
  const cards = dom.queryAll(".material-card");
  const observer = visibility.observe(cards, (entries, instance) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      waapi.animate(entry.target, [
        { opacity: 0.25, transform: "translateY(28px)" },
        { opacity: 1, transform: "translateY(0)" }
      ], {
        duration: 650,
        easing: "cubic-bezier(.16,1,.3,1)",
        fill: "both"
      });
      instance.unobserve(entry.target);
    });
  }, { threshold: 0.2 });

  return () => observer.disconnect();
}
</script>
```

## Three.js

Do not add Three.js through `scripts[]` or a CDN. `three.load()` lazy-loads the
renderer-owned package and reserves one managed WebGL context.

```html
<script
  type="application/lexsis-motion"
  data-motion-id="faceted-product"
  data-capabilities="three resize"
  data-mode="interaction"
  data-importance="decorative"
  data-reduced-motion="static"
>
async ({ dom, three, resize, scheduler, quality }) => {
  const THREE = await three.load();
  const canvas = dom.query(".product-canvas");
  if (!canvas) return;

  const renderer = new THREE.WebGLRenderer({
    canvas,
    alpha: true,
    antialias: quality.tier !== "low"
  });
  renderer.setPixelRatio(quality.dpr);

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 100);
  camera.position.z = 7;

  const geometry = new THREE.IcosahedronGeometry(1.4, 2);
  const material = new THREE.MeshPhysicalMaterial({
    color: 0x111111,
    roughness: 0.18,
    clearcoat: 1
  });
  const object = new THREE.Mesh(geometry, material);
  scene.add(object);
  scene.add(new THREE.HemisphereLight(0xffffff, 0x222222, 3));

  const fit = () => {
    const rect = canvas.getBoundingClientRect();
    renderer.setSize(Math.max(1, rect.width), Math.max(1, rect.height), false);
    camera.aspect = rect.width / Math.max(1, rect.height);
    camera.updateProjectionMatrix();
  };
  fit();
  resize.observe(canvas, fit);

  const stopLoop = scheduler.loop(() => {
    object.rotation.y += 0.004;
    renderer.render(scene, camera);
  }, { fps: quality.fps });

  return () => {
    stopLoop();
    renderer.forceContextLoss();
    renderer.dispose();
    geometry.dispose();
    material.dispose();
  };
}
</script>
```

For drag rotation, use `dom.on()` for `pointerdown`, `pointermove`,
`pointerup`, and `pointercancel` on the canvas. Use pointer capture. Keep
vertical tilt bounded and let horizontal rotation wrap when a full revolve is
appropriate.

## Raw WebGL

Use raw WebGL when the design needs a custom shader rather than a Three.js
scene:

```html
<script
  type="application/lexsis-motion"
  data-motion-id="custom-shader"
  data-capabilities="webgl resize"
  data-mode="continuous"
  data-reduced-motion="simplified"
>
({ webgl, resize, scheduler, quality }) => {
  const surface = webgl.context(".shader-canvas", { version: 2, alpha: true });
  resize.observe(surface.canvas, surface.fit);

  const stopLoop = scheduler.loop((time) => {
    const { context } = surface;
    surface.fit();
    context.clearColor(0.08, 0.03, 0.06 + Math.sin(time * 0.001) * 0.02, 1);
    context.clear(context.COLOR_BUFFER_BIT);
  }, { fps: quality.fps });

  return () => stopLoop();
}
</script>
```

Agent-authored shader compilation, buffers, uniforms, textures, and drawing
remain inside the module. The runtime owns context limits, pause/resume, and
context loss during cleanup.

## GSAP

Do not add GSAP through page scripts. The managed loader uses pinned
first-party assets with a bounded fallback.

```html
<script
  type="application/lexsis-motion"
  data-motion-id="hero-timeline"
  data-capabilities="gsap"
  data-mode="entrance"
  data-reduced-motion="simplified"
>
async ({ gsap }) => {
  return gsap.withContext((runtime) => {
    const timeline = runtime.timeline();
    timeline
      .from(".hero-title", { opacity: 0, y: 34, duration: 0.8 })
      .from(".hero-copy", { opacity: 0, y: 16, duration: 0.5 }, "-=0.35");
    return () => timeline.kill();
  });
}
</script>
```

`gsap.withContext()` scopes selectors, reverts the timeline on cleanup, and
pauses managed animations while the section is offscreen.

## Canvas 2D

Use `canvas.context2d()` and `surface.fit()` so the renderer applies the
device-quality DPR cap. Put related drawing in one `scheduler.loop()` rather
than starting one loop per particle or object.

## Motion assets

Declare every remote resource on section markup with an absolute HTTPS URL:

```html
<div
  data-motion-asset="gift-reveal"
  data-src="https://cdn.example.com/gift-reveal.json"
  hidden
></div>
```

Then load only by declared name:

```javascript
({ assets }) => assets.json("gift-reveal")
```

Use `assets.image`, `assets.lottie.mount`, `assets.rive.mount`, or
`media.source` as appropriate. Arbitrary `fetch()` is rejected.

## Progressive enhancement

- Keep meaningful copy, images, SVG, and controls present in static HTML.
- Keep content visible by default.
- Do not make an empty fixed-height canvas the only representation of
  essential content.
- Hide a static visual fallback only after the module reports ready.
- Use `data-reduced-motion="static"` when the fallback communicates the same
  information.
- Never delay pricing, variants, CTA availability, cart state, or trust
  evidence behind animation.

If a module fails or exceeds a boundary, Lexsis disables that module and keeps
the static section usable.

## Compiler and runtime boundaries

- Motion source: at most 100 KiB per page.
- Managed loops: at most 2 per section and 4 per page.
- WebGL/Three modules: at most 2 per page.
- Device tiers cap DPR at 1, 1.5, or 2 and fps at 30, 45, or 60.
- Offscreen and hidden sections pause managed work.
- Repeated callbacks over 50 ms disable only the offending module.
- Mutation storms, excessive DOM growth, and event-loop stalls disable only
  the offending module.
- Section replacement and page exit clean up listeners, observers, timers,
  loops, engine contexts, and loaded media.

The compiler rejects:

- `window`, `document`, and global browser escape hatches
- `fetch`, WebSockets, workers, and browser storage
- raw timers, animation frames, and observers
- dynamic imports and dynamic code execution
- programmatic `.click()`
- island-internal access
- unbounded loops
- use of undeclared capabilities

Use the managed context equivalents.

## MCP compile workflow

1. Author the source section and motion block in `MCP source`.
2. Call `lexsis_pages` action `compile` with complete source, head, theme CSS,
   and approved page scripts.
3. Fix every `motion_*`, `unmanaged_*`, or capability error.
4. Confirm the returned animation manifest reflects the expected engines,
   capabilities, continuous motion, and performance tier.
5. Create or update the unpublished draft only after compilation is clean.
6. Verify the hosted draft at desktop and mobile widths. A successful compile
   proves contract safety, not visual quality.

The MCP round-trips managed motion through source reads, section patches, page
bundles, and versioned drafts.
