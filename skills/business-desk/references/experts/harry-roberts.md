# Harry Roberts

Web performance, resource loading, and measurement

This reference contains original research summaries and links to public work. It does not represent the person or imply endorsement.

## Coverage

Research snapshot: October 6, 2026. Archived X posts: 199. Distinct X posts cited below: 1. Other source entries: 3. Total source entries: 4.

Archived posts are research inputs, not a fully reviewed curriculum, and are not included in this package. Cited entries may cover written excerpts, identity context, or limited visual observations. The source directory identifies the capture type. Method labels describe the original research; they are not a fresh audit or a guarantee of business results.

* This is a selected public source library, not a complete course or exhaustive timeline.
* Candidate methods need more independent subject evidence when relied upon strongly.
* Client data, implementation behavior and results require actual verification.

## Methods

### Record realistic performance measurement conditions

Original research status: supported.

Distinguish network, navigation and cache conditions and retain missing values as missing. Compare lab observations with field measurements when available.

* [Web-Perf Wednesday 005 – RUM Needs More Than a Percentile – CSS Wizardry](https://csswizardry.com/2026/08/web-perf-wednesday-005-rum-needs-more-than-a-percentile/). Author: Harry Roberts. Locator: RUM Needs Context It Can Keep. Interpret performance measurements with device, network, cache and navigation context. Missing observations should remain missing. The specific commercial RUM tool is optional; context and measurement quality matter across tools.
* [Harry Roberts, public X teaching 2020-02-24](https://x.com/csswizardry/status/1231949327322566657). Author: Harry Roberts. Locator: Root post 1231949327322566657, exact passage in preserved API text. Distinguish cold cache visits from disabling cache altogether. Record the actual test conditions; historic DevTools behavior needs rechecking.

### Expose the real critical hero content promptly

Original research status: candidate.

Identify the LCP candidate and avoid lazy loading or delayed visibility of it. Measure resource discovery, priority and rendering on the actual page.

* [Optimising Largest Contentful Paint – CSS Wizardry](https://csswizardry.com/2022/03/optimising-largest-contentful-paint/). Author: Harry Roberts. Locator: Don’t Lazy-Load Your LCP and Don’t Fade-In Your LCP. Let the critical hero content be discoverable and visible without delayed animation or lazy loading. Prioritize the actual measured candidate. Recheck current browser measurement and delivery behavior; his historical test timings are not universal.

### Balance compression, grouping and caching

Original research status: candidate.

Choose delivery strategies using actual assets, repeat visits and network conditions. Do not concatenate everything or assume one resource strategy wins universally.

* [The Three Cs: 🤝 Concatenate, 🗜️ Compress, 🗳️ Cache – CSS Wizardry](https://csswizardry.com/2023/10/the-three-c-concatenate-compress-cache/). Author: Harry Roberts. Locator: Concatenate, Compress, Cache opening tradeoffs. Balance file grouping, compression and cache behavior as connected delivery decisions. Compare tradeoffs using the client’s network and content conditions. The method is not a blanket command to combine every resource.

## Source directory

Open the original source before precise attribution or extending a method. Multiple entries may refer to the same underlying work. Company and joint authorship remain attributed to the source authors.

* [Optimising Largest Contentful Paint – CSS Wizardry](https://csswizardry.com/2022/03/optimising-largest-contentful-paint/). Author: Harry Roberts. Published: 2022-03-28. Original capture: excerpt. Underlying work: `harry-roberts:harry-lcp`.
* [Web-Perf Wednesday 005 – RUM Needs More Than a Percentile – CSS Wizardry](https://csswizardry.com/2026/08/web-perf-wednesday-005-rum-needs-more-than-a-percentile/). Author: Harry Roberts. Published: 2026-08-19. Original capture: excerpt. Underlying work: `harry-roberts:harry-rum-context`.
* [The Three Cs: 🤝 Concatenate, 🗜️ Compress, 🗳️ Cache – CSS Wizardry](https://csswizardry.com/2023/10/the-three-c-concatenate-compress-cache/). Author: Harry Roberts. Published: 2023-10-17. Original capture: excerpt. Underlying work: `harry-roberts:harry-delivery`.
* [Harry Roberts, public X teaching 2020-02-24](https://x.com/csswizardry/status/1231949327322566657). Author: Harry Roberts. Published: 2020-02-24T14:29:42+00:00. Original capture: excerpt. Underlying work: `harry-roberts:x:1231949327322566657`.
