# Andrej Karpathy

AI learning and careful implementation

This reference contains original research summaries and links to public work. It does not represent the person or their endorsement.

## Coverage

Research compiled October 2026. Source status: ready with gaps. Original text snapshots and bulk social archives are not distributed. Method labels below describe the original research, not a fresh audit of the public sources. Open the cited source before making a precise attribution or extending a method beyond this summary.

Sources summarized: 12. Repeated methods: 5. Candidates: 3.

* This is a starter library from selected material, not exhaustive research.
* No Karpathy lecture videos or interview timelines have been fully reviewed for this library.
* Deleted, protected, withheld, or unindexed posts may be unavailable. Query exhaustion is not proof of a complete archive.
* Linked videos, images, external articles, and thread parents were not ingested unless specifically identified as reviewed.
* Original post queries and any explicitly recorded thread queries cover the declared windows only. Search exhaustion is not proof of a complete account archive.
* The archive contains unreviewed research inputs. Individually inspected excerpts are recorded in the source manifest.
* Linked articles, images, videos, and missing thread context need separate review unless explicitly recorded as inspected.

## Methods

### Expose the mechanism in a small implementation

Original research status: supported.

For learning or diagnosis, make the core operation inspectable before layering convenience or scale. This is a synthesis of these educational projects, not a prohibition on production frameworks.

* [micrograd documentation](https://github.com/karpathy/micrograd/blob/master/README.md). Author: Andrej Karpathy and repository contributors. Locator: Opening project description. The small scalar implementation is positioned as an educational tool.
* [minbpe documentation](https://github.com/karpathy/minbpe/blob/master/README.md). Author: Andrej Karpathy and repository contributors. Locator: Training section, final paragraph. The author explicitly values code that the learner can inspect and understand.

### Compare behavior against an independent reference

Original research status: supported.

Where a trustworthy reference exists, compare actual outputs and meaningful tolerances after changing an implementation. Choose checks that cover the behavior at issue.

* [micrograd reference tests](https://github.com/karpathy/micrograd/blob/master/test/test_engine.py). Author: Andrej Karpathy and repository contributors. Locator: test_more_ops. A computed forward value is compared with PyTorch under a tolerance.
* [minbpe tokenizer tests](https://github.com/karpathy/minbpe/blob/master/tests/test_tokenizer.py). Author: Andrej Karpathy and repository contributors. Locator: test_gpt4_tiktoken_equality. Tokenizer output is compared with the reference implementation.

### Make explanations concrete with inspectable expected results

Original research status: supported.

Use a small example with a predicted result, run it, and discuss mismatches. This is our teaching application of the examples in the source projects.

* [micrograd documentation](https://github.com/karpathy/micrograd/blob/master/README.md). Author: Andrej Karpathy and repository contributors. Locator: Example usage, output comment. The documentation supplies numerical outputs that can be checked.
* [minbpe documentation](https://github.com/karpathy/minbpe/blob/master/README.md). Author: Andrej Karpathy and repository contributors. Locator: Quick start explanation. The small input is paired with explicit expected token IDs.

### Add complexity in stages

Original research status: supported.

Get the simplest useful behavior working before adding features whose necessity can be explained. Preserve a comparison when extending the implementation.

* [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/). Author: Andrej Karpathy. Locator: The recipe, opening paragraph. The process explicitly introduces complexity gradually.
* [minbpe documentation](https://github.com/karpathy/minbpe/blob/master/README.md). Author: Andrej Karpathy and repository contributors. Locator: Training, first option. A simpler tokenizer is offered when extra preprocessing is unnecessary.

### Inspect actual data and transformed model inputs

Original research status: supported.

Inspect representative data before model work and inspect the transformed batch just before it enters the network. Two distinct works now support this practice.

* [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/). Author: Andrej Karpathy. Locator: Become one with the data. The article directs attention to actual examples before model code.
* [Inspect the batch entering the model](https://x.com/karpathy/status/1328547710966743040). Author: Andrej Karpathy. Locator: X post 1328547710966743040, authored post text, published 2020-11-17. Inspect actual transformed inputs and labels immediately before model execution. This can expose preprocessing and sampling errors.

### Learn through concrete projects

Original research status: candidate.

Use a concrete project to drive learning, then explain the result in your own words.

* [Learn through concrete projects](https://x.com/karpathy/status/1325154823856033793). Author: Andrej Karpathy. Locator: X post 1325154823856033793, authored post text, published 2020-11-07. Use a concrete project to drive learning, then explain the result in your own words.

### Choose an output format that helps understanding

Original research status: candidate.

Consider a diagram or interactive explanation when prose alone makes a concept hard to understand.

* [Choose an output format that helps understanding](https://x.com/karpathy/status/2105819303471976479). Author: Andrej Karpathy. Locator: X post 2105819303471976479, authored post text, published 2026-10-02. Consider a diagram or interactive explanation when prose alone makes a concept hard to understand.

### Build an iterative data and evaluation process

Original research status: candidate.

Karpathy emphasizes the repeatable process around data rather than possession of a dataset alone. For an AI feature, connect new examples, evaluation, deployment, and observed results in a documented improvement process.

* [Build an iterative data and evaluation process](https://x.com/karpathy/status/1599852921541128194). Author: Andrej Karpathy. Locator: X post 1599852921541128194, authored post text, published 2022-12-05. Karpathy emphasizes the repeatable process around data rather than possession of a dataset alone. For an AI feature, connect new examples, evaluation, deployment, and observed results in a documented improvement process.

## Source summaries

### micrograd documentation

[Andrej Karpathy and repository contributors](https://github.com/karpathy/micrograd/blob/master/README.md)

The project exposes automatic differentiation through scalar operations, includes an example with expected values, and describes reference checks against PyTorch.

Original capture: full_text. Underlying work: `karpathy:micrograd`.

### micrograd reference tests

[Andrej Karpathy and repository contributors](https://github.com/karpathy/micrograd/blob/master/test/test_engine.py)

Tests compare forward values and gradients with PyTorch, using exact comparisons or an explicit tolerance. This is evidence of checking a small implementation against a reference.

Original capture: full_text. Underlying work: `karpathy:micrograd`.

### minbpe documentation

[Andrej Karpathy and repository contributors](https://github.com/karpathy/minbpe/blob/master/README.md)

The project separates basic byte pair encoding, regex preprocessing, and compatibility behavior. Its quick start gives a small input and expected tokens, while another example compares results with tiktoken.

Original capture: full_text. Underlying work: `karpathy:minbpe`.

### minbpe tokenizer tests

[Andrej Karpathy and repository contributors](https://github.com/karpathy/minbpe/blob/master/tests/test_tokenizer.py)

Tests cover encode and decode identity, Unicode and empty strings, reference token equality, special tokens, and persistence. Passing these tests was not claimed or measured in this research task.

Original capture: full_text. Underlying work: `karpathy:minbpe`.

### A Recipe for Training Neural Networks

[Andrej Karpathy](https://karpathy.github.io/2019/04/25/recipe/)

The article recommends inspecting examples before modeling and increasing complexity in stages. Treat these as neural network development guidance, with broader applications labeled as synthesis.

Original capture: excerpt. Underlying work: `karpathy:recipe-2019`.

### Neural Networks: Zero to Hero course introduction

[Andrej Karpathy](https://karpathy.ai/zero-to-hero.html)

The course teaches neural networks through implementation. Its introduction and syllabus establish educational scope; they do not substitute for review of the actual lectures.

Original capture: excerpt. Underlying work: `karpathy:zero-to-hero`.

### Official profile and source directory

[Andrej Karpathy](https://karpathy.ai/)

The public site identifies Andrej Karpathy as an AI researcher and educator and links his writing, teaching, and code. Only professional source discovery is retained here.

Original capture: research_notes. Underlying work: `karpathy:official-profile`.

### X identity and attribution check

[Andrej Karpathy](https://karpathy.ai/)

The official website links karpathy. The API profile matches Andrej Karpathy.

Locator: Official public link and API profile matched on October 5, 2026

Original capture: research_notes. Underlying work: `andrej-karpathy:x-identity-2026-10-05`.

### Inspect the batch entering the model

[Andrej Karpathy](https://x.com/karpathy/status/1328547710966743040)

Inspect actual transformed inputs and labels immediately before model execution. This can expose preprocessing and sampling errors.

Locator: X post 1328547710966743040, authored post text, published 2020-11-17

Original capture: excerpt. Underlying work: `andrej-karpathy:x-conversation-1328547710966743040`.

### Learn through concrete projects

[Andrej Karpathy](https://x.com/karpathy/status/1325154823856033793)

Use a concrete project to drive learning, then explain the result in your own words.

Locator: X post 1325154823856033793, authored post text, published 2020-11-07

Original capture: excerpt. Underlying work: `andrej-karpathy:x-conversation-1325154823856033793`.

### Choose an output format that helps understanding

[Andrej Karpathy](https://x.com/karpathy/status/2105819303471976479)

Consider a diagram or interactive explanation when prose alone makes a concept hard to understand.

Locator: X post 2105819303471976479, authored post text, published 2026-10-02

Original capture: excerpt. Underlying work: `andrej-karpathy:x-conversation-2105819303471976479`.

### Build an iterative data and evaluation process

[Andrej Karpathy](https://x.com/karpathy/status/1599852921541128194)

Karpathy emphasizes the repeatable process around data rather than possession of a dataset alone. For an AI feature, connect new examples, evaluation, deployment, and observed results in a documented improvement process.

Locator: X post 1599852921541128194, authored post text, published 2022-12-05

Original capture: excerpt. Underlying work: `andrej-karpathy:x-conversation-1599852921541128194`.
