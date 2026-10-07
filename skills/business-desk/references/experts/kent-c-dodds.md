# Kent C. Dodds

User focused website testing and maintainable implementation

This reference contains original research summaries and links to public work. It does not represent the person or imply endorsement.

## Coverage

Research snapshot: October 6, 2026. Archived X posts: 380. Distinct X posts cited below: 1. Other source entries: 4. Total source entries: 5.

Archived posts are research inputs, not a fully reviewed curriculum, and are not included in this package. Cited entries may cover written excerpts, identity context, or limited visual observations. The source directory identifies the capture type. Method labels describe the original research; they are not a fresh audit or a guarantee of business results.

* This is a selected public source library, not a complete course or exhaustive timeline.
* Candidate methods need more independent subject evidence when relied upon strongly.
* Client data, implementation behavior and results require actual verification.

## Methods

### Test the real use cases that need confidence

Original research status: supported.

Exercise observable customer tasks, meaningful failures and receiving systems. Add checks incrementally to an existing project rather than rewriting tests for tooling conformity.

* [How to know what to test](https://kentcdodds.com/blog/how-to-know-what-to-test). Author: Kent C. Dodds. Locator: Remembering why we test. Prioritize meaningful user cases that create confidence in real use, rather than treating line coverage as the objective. For client sites that includes the actual primary action and its receiving system.
* [How to add testing to an existing project](https://kentcdodds.com/blog/how-to-add-testing-to-an-existing-project). Author: Kent C. Dodds. Locator: Testing Trophy introduction and Step 1. Add checks incrementally to an existing project, starting with valuable confidence. Preserve useful existing lint, types and critical journey tests. Avoid a full test rewrite just to match the author’s tooling.
* [Kent C. Dodds, public X teaching 2018-04-01](https://x.com/kentcdodds/status/980276908217663493). Author: Kent C. Dodds. Locator: Root post 980276908217663493, exact passage in preserved API text. Exercise the use case the user actually depends on. This supports observable behavior rather than implementation mirroring.

### Confirm important checks can detect broken behavior

Original research status: candidate.

Use an isolated negative control to ensure critical tests fail for the relevant broken use case. Restore correct behavior and rerun the final checks.

* [Make Your Test Fail](https://kentcdodds.com/blog/make-your-test-fail). Author: Kent C. Dodds. Locator: Opening question and example. Confirm that important tests detect a broken behavior through an isolated negative control. Restore the correct behavior before delivery. The article’s sample password policy is not a current security recommendation.

### Query controls through roles and accessible names

Original research status: candidate.

Use observable interface roles and names when practical. Await real state changes and verify current testing tool APIs.

* [Common mistakes with React Testing Library](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library). Author: Kent C. Dodds. Locator: Using the wrong query, ByRole discussion. Query user facing roles and accessible names where practical. Tests should exercise observable behavior and await real state changes. Historical library setup details require current documentation.

## Source directory

Open the original source before precise attribution or extending a method. Multiple entries may refer to the same underlying work. Company and joint authorship remain attributed to the source authors.

* [How to know what to test](https://kentcdodds.com/blog/how-to-know-what-to-test). Author: Kent C. Dodds. Published: 2019-04-13. Original capture: excerpt. Underlying work: `kent-c-dodds:kent-user-cases`.
* [Common mistakes with React Testing Library](https://kentcdodds.com/blog/common-mistakes-with-react-testing-library). Author: Kent C. Dodds. Published: 2020-05-04. Original capture: excerpt. Underlying work: `kent-c-dodds:kent-accessible-queries`.
* [How to add testing to an existing project](https://kentcdodds.com/blog/how-to-add-testing-to-an-existing-project). Author: Kent C. Dodds. Published: 2019-10-28. Original capture: excerpt. Underlying work: `kent-c-dodds:kent-existing`.
* [Make Your Test Fail](https://kentcdodds.com/blog/make-your-test-fail). Author: Kent C. Dodds. Published: 2020-02-24. Original capture: excerpt. Underlying work: `kent-c-dodds:kent-negative-control`.
* [Kent C. Dodds, public X teaching 2018-04-01](https://x.com/kentcdodds/status/980276908217663493). Author: Kent C. Dodds. Published: 2018-04-01T02:53:22+00:00. Original capture: excerpt. Underlying work: `kent-c-dodds:x:980276908217663493`.
