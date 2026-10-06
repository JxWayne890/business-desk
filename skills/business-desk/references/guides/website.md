# Business Desk Web Design Guide

Updated October 6, 2026. Use this guide with the bundled [website build workflow](../website-build.md) and the current Business Desk routing table. It adapts the website to the client, the customer task, and the available content. The industry examples below are Business Desk applications of the reviewed teaching, not claims that every teacher has a complete course for every industry.

## Start with the client and customer

Before arranging the page, establish the business outcome, who visits, what those visitors need to decide, and what happens after the main action. Use existing notes and records first. Ask only for missing information that materially changes the build. Paul Boag’s [project assessment](https://boagworld.com/emails/introducing-supa/) and [journey mapping](https://boagworld.com/usability/customer-journey-mapping/) inform this discovery step.

Record a compact design brief:

* Business type, customer groups, offer, geography, and primary customer task.
* Primary action and destination, such as browse inventory, purchase, request a quote, book, or call.
* Questions and proof the customer needs before taking that action.
* Approved services, products, staff, locations, prices, claims, photos, and brand assets.
* Existing platform, purchased scope, integrations, data sources, and who maintains each source.
* Visual character, such as precise and technical, welcoming and personal, editorial and refined, or practical and dependable. Tie these choices to the client rather than industry stereotypes.
* A success measure tied to the actual business, such as qualified inquiries, completed appointments, or purchases. Use observed results when available.

Write the content outline and main journey before filling a template. Design and copy can then develop together. Charli Marie distinguishes the page’s required content from its final wording in [Which comes first: the design or the copy?](https://charlimarie.com/blog/design-or-copy).

## Choose the site around the task

These are starting configurations. Include modules only when the client offers the function and the project includes it. A business can combine configurations, such as an electrician selling products or a clinic operating several locations.

| Client | Main journey | Useful pages and modules | Required operational facts |
| :--- | :--- | :--- | :--- |
| Car dealership | Find a suitable vehicle, inspect it, inquire or arrange a visit | Inventory browsing, useful filters and sort, vehicle detail pages, photo galleries, availability, inquiry or test drive request, optional meaningful comparisons | Actual vehicle identifiers, year, make, model, mileage, condition, prices, stock status, dealer locations, approved photos, and inventory update source |
| Shopify store | Find the right product and variant, evaluate it, purchase | Collections, search and filters, product detail, variant selection, cart, existing Shopify checkout, delivery and return information | Real catalog, variant prices, stock, images, shipping and return policies, payment and fulfillment configuration |
| Clinic | Find an appropriate service or provider, understand the visit, request an appointment | Services, provider profiles, locations, appointment request or existing scheduler, practical visit information, actual contact details | Verified credentials, offered services, locations, scheduling rules, approved patient information, and the existing booking destination |
| Plumber, electrician, or other trade | Confirm the business handles this problem and area, then contact it | Actual services, service details, coverage areas, evidence of work, quote request, prominent phone contact, urgent service path when offered | Services, coverage, hours, contact routing, response commitments, qualifications, and approved project photos |
| Construction company | Evaluate fit and capability, inspect relevant work, discuss a project | Project portfolio, project details, capabilities, markets served, process, team information, project inquiry | Approved project credits, scope, photos, locations, capabilities, qualifications, and inquiry ownership |
| AI agency | Understand a concrete business use case, evaluate proof and fit, discuss the scope | Use cases, service detail, verified case studies, appropriate demonstrations, process, scope boundaries, discovery request | Supported capabilities, actual integrations, demonstrable results, client permission, limits, and the next sales step |

A used vehicle inventory browser and a new vehicle configurator solve different tasks. Do not substitute a configurator for live stock. Add customization only when the dealer offers it and has the necessary option, price, and availability data. Vitaly Friedman’s [responsive configurator](https://www.smashingmagazine.com/2018/02/designing-a-perfect-responsive-configurator/) discusses customization and the need to ground it in real choices.

Use comparisons where customers face meaningful tradeoffs. Choose the attributes customers actually need, rather than a long list of decorative checkmarks. Keep filter selections and result context stable, and make empty results understandable. These applications draw on Vitaly’s [comparison tables](https://www.smashingmagazine.com/2017/08/designing-perfect-feature-comparison-table/) and [filter behavior](https://www.smashingmagazine.com/2021/07/frustrating-design-patterns-broken-frozen-filters/).

Industry names alone do not determine the layout. A clinic with walk in visits differs from one with appointment selection. A dealer selling a small specialist collection differs from a large searchable catalog. Use the actual task, features, and content to choose the pattern, informed by Vitaly’s [responsive pattern discussion](https://www.smashingmagazine.com/2016/05/smart-responsive-design-patterns-or-when-off-canvas-isnt-good-enough/).

## Give each client a deliberate visual identity

Choose typography, image direction, spacing, color roles, and a recognizable visual motif before polishing individual sections. Explain how each choice supports the brand and customer task. Erik Kennedy’s [brand motif article](https://www.learnui.design/blog/spice-up-designs-create-cohesive-brand.html) shows how a motif can recur across a site. His [Hard in Figma](https://www.learnui.design/blog/hard-in-figma.html) essay encourages exploring visual treatments beyond the easiest default shapes.

Use real product, vehicle, staff, location, and project photos when they establish facts. A generated illustration can explain a concept or establish atmosphere, but must not stand in for actual inventory, completed client work, credentials, or evidence of results. Follow the existing [AI Image Prompting Guide](image-direction.md) for original illustrative assets. Social image selection still follows its existing separate guide.

Avoid repeated generic hero copy, unrelated floating dashboards, identical sections for every client, and decoration with no purpose. Cards, gradients, large type, or restrained effects can be appropriate when they suit the client. They are choices to justify, not universal bans. Charli’s [art in design](https://charlimarie.com/blog/art-in-design) supports room for expression alongside functional goals.

Use a small, consistent set of text roles. Establish hierarchy through weight, size, contrast, and spacing. Do not make every label equally prominent. Steve Schoger’s [typography guidance](https://x.com/steveschoger/status/877558258755612672) and [contrast example](https://x.com/steveschoger/status/870679289624092673) provide the reviewed basis. Inspect the result with the client’s real words, images, and data.

Keep brand decoration away from controls when it makes the action, state, or information harder to recognize. Adham Dannaway’s [practical UI examples](https://www.adhamdannaway.com/blog/ui-design/ui-design-tips-14) inform this control treatment. They are useful candidate guidance from public excerpts, not independently corroborated methods from several full works.

## Make the interface usable with real content

Place an action beside the content it affects. Select controls according to the kind and number of choices. For an unfamiliar offering, show a concrete example that helps the customer understand it. These are candidate applications of Erik’s [four interaction rules](https://www.learnui.design/blog/4-rules-intuitive-ux.html), and should be checked against the particular task.

Use persistent field labels and instructions where needed, clear required information, understandable validation, and working submission feedback. Collect only information the task needs. Adham’s [field label example](https://x.com/AdhamDannaway/status/2057107829241364656) supports the label guidance. The form pipeline determines validation, record destination, notifications, and the completed submission behavior.

Build a coherent set of navigation, buttons, fields, content patterns, and states. Inspect those components on real page types with short and long content, instead of evaluating an isolated component sheet. Paul’s [page context advice](https://x.com/boagworld/status/2090393903845224696) and [component rule advice](https://x.com/boagworld/status/2090756313034703101) are useful candidates for this workflow.

Let layout respond to the available space and content. Maintain meaningful HTML, reading order, keyboard access, and a usable fallback when enhancements are unavailable. Jen Simmons’s [intrinsic layout explanation](https://x.com/jensimmons/status/988761825218056192) and [progressive enhancement discussion](https://x.com/jensimmons/status/1666509696927145995) support this direction. The linked videos were not reviewed. Her [HTML reminder](https://x.com/jensimmons/status/966675222161248257) informs a separate candidate check for the underlying document.

Do not freeze a developing CSS proposal into a production rule. Jen’s jointly authored [Grid Lanes article](https://webkit.org/blog/17660/introducing-css-grid-lanes/) describes a preview implementation. Check current official browser and platform documentation before using newer features, and provide a suitable fallback.

## Connect the real operation

Preserve the client’s chosen platform and working integrations unless a change is requested or justified within scope. A Shopify store should retain its actual commerce flows. A dealer needs an agreed inventory source and update process. A clinic needs the intended scheduler. A service company needs inquiries to reach the actual team.

For each dynamic module, identify its source, update owner, loading behavior, error behavior, empty state, and action destination. Distinguish a visual prototype, a configured integration, and a tested working flow. Never present decorative search, simulated appointments, fake stock, or disconnected checkout as a completed feature.

Route forms, CRM records, scheduling, notifications, and launch checks through available tools and any installed specialist skills when included in the project. Design teachers guide the experience; current technical documentation and verified business records determine implementation and facts.

## Check the result

Before calling a client website ready:

1. Follow its primary journey from entry to the intended outcome. Test real routes and data, including an unavailable item, empty result, or submission error when relevant.
2. Inspect representative pages at phone, tablet, and desktop sizes. Check long text, images, menus, filters, forms, and the main action.
3. Check meaningful reading order, visible focus, keyboard operation, labels, contrast, and motion behavior. Verify applicable current standards rather than copying old numerical advice.
4. Confirm that photos, claims, credentials, inventory, prices, contact details, and commitments come from approved sources.
5. Run the project’s relevant build and checks, and verify integration outcomes. Record limitations that remain.
6. Review actual business outcomes after launch when measurement is available, then choose the next improvement. Charli’s [outcomes discussion](https://charlimarie.com/blog/outcomes-vs-output) and [use of data](https://charlimarie.com/blog/making-friends-with-data) inform that cycle. A polished design alone does not establish better conversion.

## Select the teacher by the problem

| Need | Library |
| :--- | :--- |
| Client brief, customer journey, business priorities | [Paul Boag](../experts/paul-boag.md) |
| Brand, content outline, marketing design, success measures | [Charli Marie](../experts/charli-marie.md) |
| Typography, hierarchy, spacing, UI polish | [Steve Schoger](../experts/steve-schoger.md) |
| Distinctive landing pages, motifs, intuitive interaction | [Erik Kennedy](../experts/erik-kennedy.md) |
| Catalog search, filters, comparisons, complex choices | [Vitaly Friedman](../experts/vitaly-friedman.md) |
| Forms, component consistency, practical UI detail | [Adham Dannaway](../experts/adham-dannaway.md) |
| Flexible layout, semantic structure, progressive enhancement | [Jen Simmons](../experts/jen-simmons.md) |

Use one lead and relevant supporting teaching when needed. Read the selected source pages before attributing a recommendation. The seven libraries contain 35 selected source entries, with 12 supported methods and 18 candidates. The underlying X archive is not distributed with this package. The included briefs contain the reviewed summaries and source links. Full books, paid courses, complete videos, and industry specific integration expertise remain gaps. Read the included expert briefs for coverage limits.
