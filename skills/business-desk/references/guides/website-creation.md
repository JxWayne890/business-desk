# Complete website creation

Use this guide for a complete client website, together with the [build workflow](../website-build.md) and [detailed design guide](website.md). Assess all 24 areas below. Mark each as applicable or outside the agreed scope, with a reason. Select relevant sources rather than forcing every role into every project.

The [category register](../website-categories.json) maps each area to source links, evidence limits, and acceptance conditions. Read the selected [expert briefs](../experts/index.json). Recheck applicable [official implementation references](website-standards.md) during a real build. These guides use the host's available tools; they do not install hosting, CRM, commerce, or a website runtime.

## The 24 researched areas

| Area | Lead and relevant support | Acceptance condition |
| :--- | :--- | :--- |
| 1. Business discovery and website strategy | Paul Boag; Peep Laja, Joanna Wiebe | An approved brief identifies the offer, audience, priority task, verified facts, scope, platform, constraints and measurable business outcome. |
| 2. Customer journeys and site architecture | Paul Boag; Vitaly Friedman, Knut Melvær | A page and journey map connects each entry point to a useful next action. Navigation, search and content relationships fit the customer task. |
| 3. Positioning and website copy | Joanna Wiebe; Peep Laja, Andy Crestodina | Copy names the audience, offer, relevant difference, customer problem and supported value. Each claim has facts or a disclosed gap. |
| 4. Visual and brand direction | Charli Marie; Erik Kennedy, Steve Schoger | The visual brief specifies typography, palette, spacing, imagery and a client specific motif with a rationale grounded in the brand and audience. |
| 5. Hero section structure | Joanna Wiebe; Andy Crestodina, Erik Kennedy | The first screen explains the actual offer and context, gives relevant evidence and presents the intended action. Its structure fits the business and reading order. |
| 6. Hero image design | Drew Brucker; Andy Crestodina, Ahmad Shadeed, Knut Melvær | The image brief defines subject, composition, lighting, palette, crop, text space, aspect ratios and truthful use. Generated imagery is inspected at desktop and mobile sizes. |
| 7. OG and social preview design | Lee Robinson; Janis Ozolins, Charli Marie | Each public page has appropriate title, description, canonical URL and reachable share image. A real preview or documented crawler check verifies readable crops and metadata. |
| 8. UI components and design systems | Steve Schoger; Erik Kennedy, Ahmad Shadeed | Reusable tokens and components cover actual content, hierarchy and interaction states. Repeated sections share deliberate design rules without flattening the client brand. |
| 9. Industry specific functionality | Vitaly Friedman; Kurt Elster, Knut Melvær | Required industry journeys use real structured data, update ownership and honest states. Inventory, checkout, service inquiry, clinic scheduling or agency discovery are included only when relevant and scoped. |
| 10. Forms and conversion flows | Adam Silver; Sara Soueidan, Andy Crestodina | Every scoped form has clear questions, labels, validation, recovery and submission status. A meaningful test confirms its intended receiving system and avoids duplicate submissions. |
| 11. Mobile and responsive design | Ahmad Shadeed; Jen Simmons, Sara Soueidan | Representative pages and journeys work with real content at narrow, intermediate and wide widths, zoom and applicable input types. Crops, navigation and tables remain usable. |
| 12. Accessibility | Sara Soueidan; Adam Silver, Kent C. Dodds | Keyboard, focus, labels, structure, contrast, zoom and dynamic status checks are recorded. Automated checks supplement manual checks, with current standards and any untested assistive modes stated. |
| 13. Animation and motion design | Jhey Tompkins; Sara Soueidan, Harry Roberts | Each motion has a purpose and usable fallback. Reduced motion, keyboard behavior, browser support and loading impact are checked. Core content never waits for decorative animation. |
| 14. Performance and image delivery | Harry Roberts; Ahmad Shadeed, Lee Robinson, Julius Fedorovicius | Critical content loads promptly with suitable image sizes, crop, delivery, fonts and resource budgets. Representative measurements record conditions and distinguish laboratory from field evidence. |
| 15. Technical SEO | Aleyda Solis; Lee Robinson, Marie Haynes | Public pages return expected statuses and render useful content. Canonicals, internal links, robots controls, sitemap, redirects and applicable structured data are checked against current search guidance. |
| 16. Page content and search intent | Andy Crestodina; Aleyda Solis, Marie Haynes | A page intent map covers actual services or products and customer questions. Pages provide original useful evidence and a relevant next action without bulk duplicate content. |
| 17. Local SEO | Joy Hawkins; Darren Shaw | Eligible locations and service areas use verified business facts and relevant destination pages. Current business profile and review policies are checked. No fake locations or selective review gating. |
| 18. AEO and AI discovery | Aleyda Solis; Marie Haynes, Andy Crestodina | Important answers and business facts are accessible, explicit, consistent and supported. Relevant discovery checks record platform and date. Citations, visits and business outcomes remain distinct, with no visibility guarantee. |
| 19. Trust and proof | Andy Crestodina; Joanna Wiebe, Peep Laja | Approved proof is placed beside the claim it supports and works on important entry pages. Testimonials, certifications, inventory and project evidence are genuine and current. |
| 20. Analytics and conversion improvement | Julius Fedorovicius; Andy Crestodina, Peep Laja | A measurement plan defines primary outcomes, supporting events, parameters, consent behavior and ownership. Both positive and negative event cases are tested at the receiving analytics destination. |
| 21. Integrations and content management | Knut Melvær; Lee Robinson, Kurt Elster | The data model and editorial workflow fit the business and approved platform. Each scoped integration has ownership, authentication, validation, failure handling, preview and a meaningful end to end test. |
| 22. Security, privacy, and reliability | Troy Hunt; Lee Robinson | The actual surface is reviewed for exposed secrets, authorization, unnecessary personal data, input handling and failure modes. Current platform guidance and applicable policy decisions inform the checks. |
| 23. Browser testing and quality review | Kent C. Dodds; Sara Soueidan, Harry Roberts | Real critical journeys pass in the relevant browser and size matrix, including error and empty states. Screenshots, outcomes and project checks are recorded, with untested environments stated. |
| 24. Launch, handoff, and maintenance | Lee Robinson; Kent C. Dodds, Knut Melvær | Launch checks cover the authorized environment, domains, routes, forms, assets, data and recovery. Handoff identifies ownership, editing instructions, credentials handling, backups and maintenance obligations. |

## Build with client specific direction

Start with the real customer problem and journey. Create a page map, message hierarchy, factual proof and visual brief before implementation. Select purposeful typography, hierarchy, spacing, imagery and a coherent motif based on the brand and audience. Test long service names, vehicle titles and product variants as actual content. Preserve the useful existing platform.

The hero must explain the particular offer and connect the intended action to a working destination. Its order and layout follow the visitor’s awareness and the client’s task. The image direction specifies subject, camera, composition, lighting, materials, photographic character, text space and wide and narrow crops. Use the included [image direction guide](image-direction.md) and Drew Brucker brief. Inspect the actual generated result. Use real client assets for inventory, staff, project work and proof. Illustrations cannot stand in for those facts.

OG cards communicate the specific page with clear hierarchy and intentional imagery. Use Janis Ozolins and Charli Marie for clarity and brand direction, with Lee Robinson for implementation and preview checks. Review text legibility at sharing size, crop, title, description, canonical and reachable image. Preserve the approved logo. Logo creation remains a separate task.

Motion must have a purpose and a usable static experience. Honor reduced motion, test relevant pause and input behavior, and keep the principal content visible during loading. An attractive CSS demo is not a reason to hide a hero behind an entrance animation. Performance decisions use actual critical resources, realistic test conditions and current browser support.

Build useful search content from actual services, products, locations, experience and buyer questions. Keep important information accessible and consistent with visible structured data. Avoid fabricated local locations, generic bulk service area pages, unsupported results and selective review gating. AI visibility, citations, visits and business outcomes are separate measurements. No inclusion or ranking is guaranteed.

## Implementation and handoff

Preserve the client platform and actual scope. Implement only authorized integrations with their real data sources, receiving systems, failure behavior, and ownership. A prototype form is not a verified submission flow. Client website, backend, booking, notification, dashboard, voice, and deployment tools are supplied separately by the host when needed.

Record checks for responsive layouts, keyboard use, focus, labels, error states, customer actions, analytics, and data access. Distinguish actual browser and integration results from a design review. Report untested environments and unresolved dependencies.

Handoff covers editing, accounts, data ownership, backups, recovery, and maintenance obligations. Logo creation remains a separate task. Source coverage is partial; a listed category does not imply every teacher covers every industry or that a business outcome is guaranteed.
