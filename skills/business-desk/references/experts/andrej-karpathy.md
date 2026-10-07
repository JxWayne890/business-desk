# Andrej Karpathy

AI learning and careful implementation

This reference contains original research summaries and links to public work. It does not represent the person or imply endorsement.

## Coverage

Research snapshot: October 6, 2026. Archived X posts: 2,728. Distinct X posts cited below: 4. Other source entries: 8. Total source entries: 12.

Archived posts are research inputs, not a fully reviewed curriculum, and are not included in this package. Cited entries may cover written excerpts, identity context, or limited visual observations. The source directory identifies the capture type. Method labels describe the original research; they are not a fresh audit or a guarantee of business results.

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

## Source directory

Open the original source before precise attribution or extending a method. Multiple entries may refer to the same underlying work. Company and joint authorship remain attributed to the source authors.

* [micrograd documentation](https://github.com/karpathy/micrograd/blob/master/README.md). Author: Andrej Karpathy and repository contributors. Published: unknown. Original capture: full_text. Underlying work: `karpathy:micrograd`.
* [micrograd reference tests](https://github.com/karpathy/micrograd/blob/master/test/test_engine.py). Author: Andrej Karpathy and repository contributors. Published: unknown. Original capture: full_text. Underlying work: `karpathy:micrograd`.
* [minbpe documentation](https://github.com/karpathy/minbpe/blob/master/README.md). Author: Andrej Karpathy and repository contributors. Published: unknown. Original capture: full_text. Underlying work: `karpathy:minbpe`.
* [minbpe tokenizer tests](https://github.com/karpathy/minbpe/blob/master/tests/test_tokenizer.py). Author: Andrej Karpathy and repository contributors. Published: unknown. Original capture: full_text. Underlying work: `karpathy:minbpe`.
* [A Recipe for Training Neural Networks](https://karpathy.github.io/2019/04/25/recipe/). Author: Andrej Karpathy. Published: 2019-04-25. Original capture: excerpt. Underlying work: `karpathy:recipe-2019`.
* [Neural Networks: Zero to Hero course introduction](https://karpathy.ai/zero-to-hero.html). Author: Andrej Karpathy. Published: unknown. Original capture: excerpt. Underlying work: `karpathy:zero-to-hero`.
* [Official profile and source directory](https://karpathy.ai/). Author: Andrej Karpathy. Published: unknown. Original capture: research_notes. Underlying work: `karpathy:official-profile`.
* [X identity and attribution check](https://karpathy.ai/). Author: Andrej Karpathy. Published: unknown. Original capture: research_notes. Underlying work: `andrej-karpathy:x-identity-2026-10-05`.
* [Inspect the batch entering the model](https://x.com/karpathy/status/1328547710966743040). Author: Andrej Karpathy. Published: 2020-11-17. Original capture: excerpt. Underlying work: `andrej-karpathy:x-conversation-1328547710966743040`.
* [Learn through concrete projects](https://x.com/karpathy/status/1325154823856033793). Author: Andrej Karpathy. Published: 2020-11-07. Original capture: excerpt. Underlying work: `andrej-karpathy:x-conversation-1325154823856033793`.
* [Choose an output format that helps understanding](https://x.com/karpathy/status/2105819303471976479). Author: Andrej Karpathy. Published: 2026-10-02. Original capture: excerpt. Underlying work: `andrej-karpathy:x-conversation-2105819303471976479`.
* [Build an iterative data and evaluation process](https://x.com/karpathy/status/1599852921541128194). Author: Andrej Karpathy. Published: 2022-12-05. Original capture: excerpt. Underlying work: `andrej-karpathy:x-conversation-1599852921541128194`.
