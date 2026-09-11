# Product grid mechanics

The collection contract in `references/page-types/collection-landing.md`
owns product count, filtering decisions, placement, and card content.
This file only implements a static, accessible product list.

## Source shape

```html
<!-- section: product-grid -->
<section id="product-grid" class="px-4 py-16">
  <h2>Explore the collection</h2>
  <ul class="grid grid-cols-2 gap-4 lg:grid-cols-4">
    <li>
      <article>
        <a href="{{PRODUCT_URL}}" class="block min-h-[48px]">
          <img src="{{IMAGE_URL}}" alt="{{PRODUCT_ALT}}"
               width="640" height="800" loading="lazy">
          <h3>{{PRODUCT_TITLE}}</h3>
        </a>
        <p>{{PRODUCT_PRICE}}</p>
      </article>
    </li>
  </ul>
</section>
```

Bind every token to real catalogue data before compiling. Repeat the article
for each selected product; the product link is navigation, not an add-to-cart
substitute. Reviews and price annotations follow the type's proof/offer
references rather than fabricated card metadata.

## Interaction boundary

Resolve quick-add or variant selection through
`references/workflows/island-selection-workflow.md`. Keep its actual product
binding and current availability; do not attach a parallel cart handler.
Native links remain usable before hydration. Additional images may be
explicitly selected or horizontally scrolled by the shopper; do not rotate
card images on timers or hijack wheel input. See `references/scroll-patterns.md`.

For bundles or complementary products, the type and
`references/consumer-behavior-cro.md` determine the relationship. A generic
product list is not evidence that the products belong together.
