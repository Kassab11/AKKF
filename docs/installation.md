# Installation

[Back to the overview](../README.md)

This repository integrates with Stone Soup by adding two helper modules and replacing its Kalman predictor and updater modules. Use a dedicated environment so the supplied research components are kept separate from other Stone Soup projects.

## 1. Prepare an environment

Create a Python virtual environment from the repository directory:

```bash
python -m venv .venv
```

Activate it using the command for your shell:

| Shell | Command |
| --- | --- |
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows Command Prompt | `.venv\Scripts\activate.bat` |
| macOS or Linux | `source .venv/bin/activate` |

Install Stone Soup and the libraries used by the notebook:

```bash
python -m pip install stonesoup numpy scipy matplotlib jupyterlab ipykernel
```

This follows Stone Soup's [standard pip installation](https://stonesoup.readthedocs.io/en/stable/#installation). Choose a Python version supported by the Stone Soup release you install.

**Compatibility status:** the original repository does not identify a tested Stone Soup release or exact dependency versions. The command above installs the releases selected by pip; it is not a validated reproduction environment. The supplied replacement modules may depend on Stone Soup APIs from the original implementation period.

If you already have the environment used for the research, preserve its dependency versions instead of upgrading it.

## 2. Locate the Stone Soup package

Run this command in the activated environment:

```bash
python -c "from pathlib import Path; import stonesoup; print(Path(stonesoup.__file__).resolve().parent)"
```

The printed directory is the **Stone Soup package directory** used in the next step. It should belong to the isolated environment you created.

## 3. Place the supplied modules

Keep a copy of the existing Stone Soup files before replacing them. Use the exact source-to-destination mapping below:

| Repository file | Destination inside the Stone Soup package directory |
| --- | --- |
| `Generator.py` | `Generator.py` |
| `kernel.py` | `kernel.py` |
| `predictor/kalman.py` | `predictor/kalman.py` |
| `updater/kalman.py` | `updater/kalman.py` |

Both replacement files are named **`kalman.py`**. Keep `Generator.py` capitalized exactly as shown because the updater imports that module by name.

The resulting package locations should look like this:

```text
<environment>/.../site-packages/stonesoup/
├── Generator.py
├── kernel.py
├── predictor/
│   └── kalman.py
└── updater/
    └── kalman.py
```

These files are part of a package: run the notebook through the environment, rather than executing the replacement `kalman.py` modules directly.

## 4. Check the imports

In the same environment, run:

```bash
python -c "from stonesoup.predictor.kalman import AdaptiveKernelKalmanPredictor; from stonesoup.updater.kalman import AdaptiveKernelKalmanUpdater; print('AKKF imports available')"
```

A successful import confirms that Python can find the supplied components. It does not establish numerical correctness or reproduce the manuscript's experiments.

## 5. Run the example

Register the environment as a notebook kernel:

```bash
python -m ipykernel install --user --name akkf --display-name "Python (AKKF)"
```

Start JupyterLab from the repository directory:

```bash
python -m jupyterlab
```

Open `sample.ipynb`, choose **Python (AKKF)**, and run the cell. The notebook creates the simulated trajectory, runs AKKF, displays a trajectory plot, and calls `savefig("tracks Vs GT")` in the notebook's working directory. Matplotlib determines the output format from its configuration.

Restart the notebook kernel after replacing any imported Stone Soup modules.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| `ModuleNotFoundError: stonesoup` | Ensure Stone Soup is installed in the interpreter used by the notebook kernel. |
| AKKF predictor or updater cannot be imported | Check both destination paths and restart the kernel after copying the modules. |
| An import refers to an unavailable Stone Soup symbol | Check the installed Stone Soup version; the repository does not yet specify a tested compatibility range. |
| `Generator` or `kernel` cannot be imported | Check file placement and capitalization inside the Stone Soup package directory. |
| The trajectory differs from a research figure | Check model settings, random seed, particle count, plotted quantity, and dependency versions. The example does not reproduce every manuscript scenario. |

When reporting a problem, include the full traceback and the environment information described in [CONTRIBUTING.md](../CONTRIBUTING.md).
