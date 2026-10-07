# Current website implementation references

Selected official requirements inspected on October 6, 2026. Recheck the relevant platform during a real build. These sources establish platform requirements, not an expert’s independent teaching.

## google-ai

Google’s AI search features require normal indexing and snippet eligibility, without additional technical requirements or a special AI schema or file. Useful text, crawl access, internal links and visible matching structured data remain relevant. Inclusion is not guaranteed.

Source: [AI Features and Your Website | Google Search Central  |  Documentation  |  Google for Developers](https://developers.google.com/search/docs/appearance/ai-features). Inspected scope: Technical requirements and best practices.

## google-seo

Make useful public pages discoverable through descriptive links and coherent structure. Apply the actual platform’s metadata and crawling controls. Search snippets and indexing are controlled by search systems, not guaranteed by site code.

Source: [SEO Starter Guide: The Basics | Google Search Central  |  Documentation  |  Google for Developers](https://developers.google.com/search/docs/fundamentals/seo-starter-guide). Inspected scope: Useful content, descriptive links and page organization.

## wcag

Focus Visible and Focus Not Obscured Minimum are AA. Focus Appearance is AAA. Minimum target size is 24 by 24 CSS pixels with stated exceptions. Test applicable criteria and usability, including sticky elements, keyboard operation, meaningful names, zoom and status. Do not equate one automated audit with complete conformance.

Source: [How to Meet WCAG (Quickref Reference)](https://www.w3.org/WAI/WCAG22/quickref/). Inspected scope: Criteria 2.4.7, 2.4.11, 2.4.13 and 2.5.8.

## web-vitals

Good thresholds are LCP at most 2.5 seconds, INP at most 200 milliseconds and CLS at most 0.1 at the 75th percentile, segmented by mobile and desktop. Field qualification requires real observations. Laboratory measurements guide development but do not establish field success.

Source: [Web Vitals  |  Articles  |  web.dev](https://web.dev/articles/vitals). Inspected scope: Core Web Vitals thresholds and measurement.

## og

The core OG properties are title, type, image and URL. Description and relevant image properties support useful previews. Inspect reachable URLs, page specific content and readable crops. The protocol does not establish a universal optimal card size for every platform.

Source: [The Open Graph protocol](https://ogp.me/). Inspected scope: Basic metadata and structured image properties.

## next-metadata

When the actual project uses the Next App Router, apply its current metadata exports, generation and file conventions. Server component constraints apply. This example does not justify migrating other platforms.

Source: [Getting Started: Metadata and OG images | Next.js](https://nextjs.org/docs/app/getting-started/metadata-and-og-images). Inspected scope: Metadata API, file conventions and OG images.

## owasp-authorization

Explicitly deny unauthorized access and verify permission checks for each protected request and resource. Frontend hiding is not authorization. Framework defaults and account roles require verification in the actual client environment.

Source: [Authorization - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). Inspected scope: Deny by default and validate permissions on every request.

## google-local

Use eligible real locations and correct service area facts. A virtual office is not automatically eligible. Service businesses without a customer facing storefront must follow the applicable address and service area rules. Website pages must not invent business locations.

Source: [Guidelines for representing your business on Google - Google Business Profile Help](https://support.google.com/business/answer/3038177). Inspected scope: Service area businesses and actual locations.

## shopify-product

A Shopify product page exposes actual product content and media, variant selection, quantity and its product form. Preserve the merchant’s cart and checkout configuration. A visually selectable option is not a verified available variant or completed purchase.

Source: [Shopify product template reference](https://shopify.dev/docs/storefronts/themes/architecture/templates/product). Inspected scope: Product object, product form, variant selector and quantity.

## focus-current

Provide a visible keyboard focus mode and maintain the indicator while focus is shown. W3C identifies this criterion as AA. It explains the relationship to Non Text Contrast and the distinct AAA Focus Appearance guidance.

Source: [Understanding Success Criterion 2.4.7: Focus Visible | WAI | W3C](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible). Inspected scope: Focus Visible AA and relationship to other criteria.

## reduced-motion

Use the reduced motion media feature to detect a request to remove, reduce or replace nonessential motion. Check the actual static experience and current browser support, without hiding essential information.

Source: [prefers-reduced-motion CSS media feature - CSS | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion). Inspected scope: Media feature syntax and reduce preference.

## google-reviews

Google prohibits discouraging negative reviews or selectively soliciting positive reviews. Genuine review requests without incentives or influence are permitted. Verify the current policy before implementing a review request workflow.

Source: [Prohibited & restricted content - Maps User Generated Content Policy Help](https://support.google.com/contributionpolicy/answer/7400114?hl=en). Inspected scope: Rating manipulation, merchant restrictions.
