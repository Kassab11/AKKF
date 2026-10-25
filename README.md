# AKKF

### Adaptive Kernel Kalman Filter for tracking research

A Python research implementation of the **Adaptive Kernel Kalman Filter (AKKF)** built on the [Stone Soup tracking library](https://stonesoup.readthedocs.io/en/stable/). The repository provides custom prediction and update components, quadratic kernel utilities, and a notebook demonstrating two-dimensional tracking with simulated measurements.

**Independent research:** this repository is maintained by Mohamad Kassab as independent research. He has no affiliation with the Stone Soup project. This work is not an official Stone Soup project and is not sponsored or endorsed by Stone Soup or its developers.

[Installation](docs/installation.md) · [Example notebook](sample.ipynb) · [Implementation notes](docs/implementation.md) · [Paper and citation](docs/research.md) · [License](LICENSE) · [Contributing](CONTRIBUTING.md)

## Overview

AKKF represents a state distribution using particles and kernel features. This implementation propagates particles through a motion model, updates kernel weights and covariance using measurements, and generates a new particle set from the estimated state moments.

The code accompanies work on comparing AKKF and Extended Kalman Filter (EKF) approaches to drone tracking.

## Associated paper

**Tracking Drones with Adaptive Kalman Filter: Adaptive versus Non-Adaptive Kernel Approach**

Raed Abu Zitar and Mohamad Kassab

Accepted for presentation at the **2026 International Conference on Control, Energy, and Smart Systems (CESS 2026)**, October 28–30, 2026, Hammamet, Tunisia.

Please cite the paper when using this work in research. See [research context and citation](docs/research.md#citing-the-work) for the reference, BibTeX entry, and the study's scope. The confirmed status is acceptance for presentation; a final proceedings citation and DOI are not yet recorded here.

## What is included

- **Custom predictor and updater** integrated into Stone Soup's Kalman modules.
- **Quadratic kernel utilities** for the implementation's feature-space calculations.
- **Gaussian particle generation** using SciPy.
- **A self-contained simulation notebook** with a four-dimensional state, noisy position measurements, and a trajectory plot.

The notebook is an illustrative AKKF example. It does not contain the complete multi-scenario AKKF–EKF evaluation described in the manuscript.

## Getting started

1. Clone the repository:

   ```bash
   git clone https://github.com/Kassab11/AKKF.git
   cd AKKF
   ```

2. Create an isolated Python environment and install Stone Soup and the notebook dependencies using the [installation guide](docs/installation.md).
3. Copy the four supplied implementation files into the matching locations in that environment's Stone Soup package, as documented in the guide.
4. Open `sample.ipynb` with the same environment selected as the notebook kernel and run its cell.

**Integration model:** this repository supplies replacement Stone Soup modules; it is not an independently installable Python package. A tested Stone Soup version and dependency lockfile are not currently recorded, so compatibility with an arbitrary release should be checked before attempting to reproduce results.

## Repository structure

| Path | Purpose |
| --- | --- |
| [`sample.ipynb`](sample.ipynb) | Simulated tracking example and trajectory visualization |
| [`predictor/kalman.py`](predictor/kalman.py) | Stone Soup Kalman predictors, including `AdaptiveKernelKalmanPredictor` |
| [`updater/kalman.py`](updater/kalman.py) | Stone Soup Kalman updaters, including `AdaptiveKernelKalmanUpdater` |
| [`kernel.py`](kernel.py) | `quadratic_kernel` and `quadratic_feature_mapping` |
| [`Generator.py`](Generator.py) | Gaussian particle sampling helper |
| [`docs/installation.md`](docs/installation.md) | Environment setup, file mapping, and import checks |
| [`docs/implementation.md`](docs/implementation.md) | Data flow, example settings, outputs, and reproducibility notes |
| [`docs/research.md`](docs/research.md) | Manuscript context, citation, and relationship to the repository |

## Example at a glance

The notebook models a single target with state **[x, vx, y, vy]** and observes the two position components.

| Setting | Value in `sample.ipynb` |
| --- | --- |
| Motion model | Two constant-velocity components |
| Process-noise coefficients | `q_x = 0.2`, `q_y = 1` |
| Measurement model | `LinearGaussian`, state mapping `(0, 2)` |
| Measurement covariance | `diag(0.1, 0.1)` |
| Initial state | `[0, 1, 0, 1]` |
| Particles | `500` |
| Random seed | `1600` |
| Simulation | 20 one-second transitions, plus the initial state |
| Kernel update settings | `alpha = 1`, `c = 1`, `k = 1e-3` |

The final plot compares the mean **predicted particle positions** with ground truth. Updated state means are stored separately in `E_buff`. See the [implementation notes](docs/implementation.md) for details needed to interpret the plotted output.

## Research and reproducibility

The associated study examines how tracking quality, tuning sensitivity, and computational demands affect filter choice. Its conclusion favors EKF as a sufficient and often preferable option for the simulated typical tracking scenarios. This is a conclusion about the reported experiments, rather than a claim that either filter dominates in every setting.

For reproducible work, record the repository commit, Python and dependency versions, model settings, particle count, and random seed alongside the outputs. The [implementation notes](docs/implementation.md#reproducibility) identify the additional context needed for comparisons with the manuscript.

## Questions and contributions

Use [GitHub Issues](https://github.com/Kassab11/AKKF/issues) for reproducible problems and documentation questions. Include the environment details and the smallest example that demonstrates the issue. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change.

## Acknowledgments

This research builds on the [Stone Soup tracking framework](https://github.com/dstl/Stone-Soup).
