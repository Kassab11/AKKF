# Research context

[Back to the overview](../README.md)

## Associated manuscript

**Tracking Drones with Adaptive Kalman Filter: Adaptive versus Non-Adaptive Kernel Approach**

Raed Abu Zitar and Mohamad Kassab

Accepted for presentation at the **2026 International Conference on Control, Energy, and Smart Systems (CESS 2026)**, October 28–30, 2026, Hammamet, Tunisia.

The title and author spellings above follow the supplied manuscript. Acceptance for presentation is the confirmed status; a proceedings publication, DOI, and final bibliographic record are not established here.

## Study focus

The work investigates AKKF for tracking a single drone under different simulated scenarios and compares it with EKF. It examines the effects of parameter tuning and particle count, and discusses the balance between tracking quality and algorithmic complexity.

The manuscript concludes that EKF provides sufficient quality and reliability in most of its simulated typical tracking scenarios, while AKKF introduces additional complexity and tuning sensitivity. This conclusion should be interpreted within the study's models, settings, and evaluation conditions.

## Relationship to this repository

The manuscript explicitly links to this repository as an implementation used in the study. The repository contains custom AKKF components and one illustrative notebook. It does not include the complete multi-scenario benchmark, the full report, or the accepted manuscript PDF.

The full report provides additional theoretical development and experimental context. Its broader experiment descriptions should not be read as features already implemented by the example notebook.

## Stone Soup attribution and independence

This research uses the [Stone Soup tracking library](https://github.com/dstl/Stone-Soup). The supplied predictor and updater modules contain adapted Stone Soup code; the upstream copyright and MIT permission notice are preserved in [LICENSES/Stone-Soup-MIT.txt](../LICENSES/Stone-Soup-MIT.txt). See [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) for attribution and license scope.

Mohamad Kassab carried out this work independently of the Stone Soup project and has no affiliation with it. This repository and the associated study are not official Stone Soup work and are not sponsored or endorsed by Stone Soup or its developers. The findings and research modifications are the authors' responsibility.

The paper credits earlier AKKF research by Mengwei Sun and colleagues, as well as the Stone Soup implementation work by James S. Wright and colleagues. This repository applies and studies those research ideas; it does not claim to originate the AKKF method.

## Citing the work

Until the final publication record is available, an acceptance-aware reference is:

> Raed Abu Zitar and Mohamad Kassab. “Tracking Drones with Adaptive Kalman Filter: Adaptive versus Non-Adaptive Kernel Approach.” Manuscript accepted for presentation at CESS 2026, Hammamet, Tunisia, October 28–30, 2026.

```bibtex
@unpublished{abuzitar_kassab_2026_drone_tracking,
  author = {Abu Zitar, Raed and Kassab, Mohamad},
  title  = {Tracking Drones with Adaptive Kalman Filter:
            Adaptive versus Non-Adaptive Kernel Approach},
  year   = {2026},
  note   = {Accepted for presentation at the 2026 International Conference
            on Control, Energy, and Smart Systems (CESS 2026),
            Hammamet, Tunisia, October 28--30, 2026}
}
```

Update this reference when a verified proceedings record becomes available. No DOI, publisher, page range, or proceedings publication status is asserted by this entry.

For software use, also include the repository URL and the exact commit used:

> AKKF repository. https://github.com/Kassab11/AKKF. Commit: [insert the output of `git rev-parse HEAD`].

## Background resources

- [Stone Soup documentation](https://stonesoup.readthedocs.io/en/stable/) — framework documentation and tracking tutorials.
- [Stone Soup repository](https://github.com/dstl/Stone-Soup) — upstream implementation and project history.
- The associated manuscript's reference list — background on kernel mean embedding, the kernel Kalman rule, AKKF, and related Stone Soup implementations.
