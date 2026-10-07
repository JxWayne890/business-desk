# Sara Soueidan

Inclusive web interface design and accessibility

This reference contains original research summaries and links to public work. It does not represent the person or imply endorsement.

## Coverage

Research snapshot: October 6, 2026. Archived X posts: 251. Distinct X posts cited below: 2. Other source entries: 5. Total source entries: 7.

Archived posts are research inputs, not a fully reviewed curriculum, and are not included in this package. Cited entries may cover written excerpts, identity context, or limited visual observations. The source directory identifies the capture type. Method labels describe the original research; they are not a fresh audit or a guarantee of business results.

* This is a selected public source library, not a complete course or exhaustive timeline.
* Candidate methods need more independent subject evidence when relied upon strongly.
* Client data, implementation behavior and results require actual verification.

## Methods

### Make keyboard focus clearly visible

Original research status: supported.

Inspect focus against actual backgrounds, clipping and overlays. Preserve usable focus and distinguish current conformance requirements from historical browser examples.

* [A guide to designing accessible, WCAG-conformant focus indicators](https://www.sarasoueidan.com/blog/focus-indicators/). Author: Sara Soueidan. Locator: Introduction and focus indicator requirements. Visible focus enables keyboard and assistive input navigation. Test visibility against actual backgrounds and sticky overlays. Recheck current WCAG requirements and distinguish AA and AAA rather than treating every focus criterion as the same conformance level.
* [Sara Soueidan, public X teaching 2019-08-12](https://x.com/SaraSoueidan/status/1160912757157486592). Author: Sara Soueidan. Locator: Root post 1160912757157486592, exact passage in preserved API text. Inspect contrast and visibility on the actual component backgrounds. Historical browser appearances are not current defaults.

### Match visible controls with accessible names

Original research status: candidate.

Use meaningful visible labels and keep them represented in accessible names. Check screen reader and speech input context for repeated actions.

* [Accessible Text Labels For All](https://www.sarasoueidan.com/blog/accessible-text-labels/). Author: Sara Soueidan. Locator: Closing thoughts: Provide visual labels whenever possible. Make control names visible and meaningful for speech input as well as screen readers. Match the visible label with the accessible name. Icon only controls need a deliberate accessible alternative and testing.

### Communicate meaningful status changes

Original research status: candidate.

Expose submission and result statuses with appropriate semantics after determining whether context already communicates them.

* [Accessible notifications with ARIA Live Regions (Part 1)](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/). Author: Sara Soueidan. Locator: Status messages in WCAG, author explanation. Expose meaningful dynamic result and submission status changes to assistive technology. Determine whether the context already changes before adding announcements. Do not flood users with indiscriminate live regions.

### Art direct images for the available space

Original research status: candidate.

Choose wide and narrow crops deliberately and verify supported browser mechanisms. A proposed picture API is not a shipped feature.

* [Component-level art direction with CSS Container Queries](https://www.sarasoueidan.com/blog/component-level-art-direction-with-container-queries-and-picture/). Author: Sara Soueidan. Locator: Card component art direction example. Plan crops for the actual component space. The article proposes extending container awareness to picture sources; that proposal is not automatically an implemented browser feature. Use current supported picture, source, sizes, object fit, and crop capabilities.

## Source directory

Open the original source before precise attribution or extending a method. Multiple entries may refer to the same underlying work. Company and joint authorship remain attributed to the source authors.

* [Accessible Text Labels For All](https://www.sarasoueidan.com/blog/accessible-text-labels/). Author: Sara Soueidan. Published: 2021-03-17. Original capture: excerpt. Underlying work: `sara-soueidan:sara-labels`.
* [A guide to designing accessible, WCAG-conformant focus indicators](https://www.sarasoueidan.com/blog/focus-indicators/). Author: Sara Soueidan. Published: 2023-08-27. Original capture: excerpt. Underlying work: `sara-soueidan:sara-focus`.
* [Accessible notifications with ARIA Live Regions (Part 1)](https://www.sarasoueidan.com/blog/accessible-notifications-with-aria-live-regions-part-1/). Author: Sara Soueidan. Published: unknown. Original capture: excerpt. Underlying work: `sara-soueidan:sara-status`.
* [Component-level art direction with CSS Container Queries](https://www.sarasoueidan.com/blog/component-level-art-direction-with-container-queries-and-picture/). Author: Sara Soueidan. Published: unknown. Original capture: excerpt. Underlying work: `sara-soueidan:sara-art-direction`.
* [Sara Soueidan, public X teaching 2024-06-07](https://x.com/SaraSoueidan/status/1799089082686902680). Author: Sara Soueidan. Published: 2024-06-07T14:40:37+00:00. Original capture: excerpt. Underlying work: `sara-soueidan:x:1799089082686902680`.
* [Sara Soueidan, public X teaching 2019-08-12](https://x.com/SaraSoueidan/status/1160912757157486592). Author: Sara Soueidan. Published: 2019-08-12T13:55:44+00:00. Original capture: excerpt. Underlying work: `sara-soueidan:x:1160912757157486592`.
* [Focus contrast illustration inspection](https://www.sarasoueidan.com/blog/focus-indicators/). Author: Sara Soueidan. Published: unknown. Original capture: visual_notes. Underlying work: `sara-soueidan:sara-focus`.
