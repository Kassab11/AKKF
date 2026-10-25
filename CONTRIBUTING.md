# Contributing

Thank you for helping improve the clarity and reproducibility of this research implementation.

## Reporting a problem

Open a [GitHub issue](https://github.com/Kassab11/AKKF/issues) with:

- the repository commit and any local changes;
- your operating system and Python, Stone Soup, NumPy, and SciPy versions;
- the setup steps you followed and the notebook kernel you selected;
- a small example that demonstrates the problem;
- the expected result, actual result, and complete traceback when applicable.

For numerical questions, also include the random seed, particle count, model settings, kernel parameters, and the quantity being evaluated. A plot of predicted positions and a plot of updated state means describe different outputs.

## Proposing a change

Keep each pull request focused on one purpose. Describe the problem, the resulting behavior, and the checks you performed. Clearly identify whether the change affects documentation, implementation, or experimental results.

For documentation updates, verify referenced paths, commands, and claims against the source. Keep research conclusions qualified by their experimental scope, and distinguish manuscript results from outputs that the included notebook actually computes.

For implementation changes, explain any effect on the filter equations, state layout, randomness, dependency compatibility, or numerical behavior. Include evidence appropriate to the change; do not describe unexecuted checks as passing tests.

Avoid unrelated notebook output changes and generated experiment files. Research documents or third-party assets should be included only when their redistribution is authorized.
