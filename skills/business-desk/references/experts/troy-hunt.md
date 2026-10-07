# Troy Hunt

Web security, privacy practices, and reliable operation

This reference contains original research summaries and links to public work. It does not represent the person or imply endorsement.

## Coverage

Research snapshot: October 6, 2026. Archived X posts: 489. Distinct X posts cited below: 1. Other source entries: 3. Total source entries: 4.

Archived posts are research inputs, not a fully reviewed curriculum, and are not included in this package. Cited entries may cover written excerpts, identity context, or limited visual observations. The source directory identifies the capture type. Method labels describe the original research; they are not a fresh audit or a guarantee of business results.

* This is a selected public source library, not a complete course or exhaustive timeline.
* Candidate methods need more independent subject evidence when relied upon strongly.
* Client data, implementation behavior and results require actual verification.

## Methods

### Minimize and inspect personal data exposure

Original research status: supported.

Verify authorization for response fields and collect only approved necessary information. Avoid promising complete erasure of copies once data spreads.

* [Troy Hunt: How Spoutible’s Leaky API Spurted out a Deluge of Personal Data](https://www.troyhunt.com/how-spoutibles-leaky-api-spurted-out-a-deluge-of-personal-data/). Author: Troy Hunt. Locator: API response disclosure analysis. Review what an endpoint actually returns and whether the caller is authorized for every field. His case exposes the danger of leaking private account data through a public profile response. Do not copy or retain breached personal data.
* [Troy Hunt: Swimming Pools, Pee, and Trying to Delete Your Data From the Internet](https://www.troyhunt.com/swimming-pools-pee-and-trying-to-delete-your-data-from-the-internet/). Author: Troy Hunt. Locator: Opening explanation of irreversibility. Minimize avoidable exposure of personal information and avoid absolute promises to erase every copy. Privacy and retention choices must match actual data collection and the client’s approved policy.

### Consider phishing resistance with usable recovery

Original research status: candidate.

Evaluate passkeys within the chosen platform and threat model when authentication is required. Verify recovery and account lifecycle rather than assuming one method secures the whole site.

* [Troy Hunt: Passkeys for Normal People](https://www.troyhunt.com/passkeys-for-normal-people/). Author: Troy Hunt. Locator: Opening phishing incident explanation. Design authentication around its real threat model. Passkeys can reduce phishing exposure where supported, with recovery and client platform needs considered. Do not treat any authentication method as a complete security program.

## Source directory

Open the original source before precise attribution or extending a method. Multiple entries may refer to the same underlying work. Company and joint authorship remain attributed to the source authors.

* [Troy Hunt: Passkeys for Normal People](https://www.troyhunt.com/passkeys-for-normal-people/). Author: Troy Hunt. Published: 2025-05-05. Original capture: excerpt. Underlying work: `troy-hunt:troy-phishing`.
* [Troy Hunt: How Spoutible’s Leaky API Spurted out a Deluge of Personal Data](https://www.troyhunt.com/how-spoutibles-leaky-api-spurted-out-a-deluge-of-personal-data/). Author: Troy Hunt. Published: 2024-02-05. Original capture: excerpt. Underlying work: `troy-hunt:troy-api-data`.
* [Troy Hunt: Swimming Pools, Pee, and Trying to Delete Your Data From the Internet](https://www.troyhunt.com/swimming-pools-pee-and-trying-to-delete-your-data-from-the-internet/). Author: Troy Hunt. Published: 2026-07-03. Original capture: excerpt. Underlying work: `troy-hunt:troy-privacy`.
* [Troy Hunt, public X teaching 2025-05-05](https://x.com/troyhunt/status/1919304532280201558). Author: Troy Hunt. Published: 2025-05-05T08:13:54+00:00. Original capture: excerpt. Underlying work: `troy-hunt:troy-phishing`.
