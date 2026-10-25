# Third-party notices

## Stone Soup

This repository builds on [Stone Soup](https://github.com/dstl/Stone-Soup), the open-source tracking and state-estimation library. The following files include adapted upstream code alongside the research additions:

| Repository file | Corresponding upstream source |
| --- | --- |
| [`predictor/kalman.py`](predictor/kalman.py) | [`stonesoup/predictor/kalman.py`](https://github.com/dstl/Stone-Soup/blob/v1.2/stonesoup/predictor/kalman.py) |
| [`updater/kalman.py`](updater/kalman.py) | [`stonesoup/updater/kalman.py`](https://github.com/dstl/Stone-Soup/blob/v1.2/stonesoup/updater/kalman.py) |
| [`sample.ipynb`](sample.ipynb) (simulation setup) | [`docs/tutorials/01_KalmanFilterTutorial.py`](https://github.com/dstl/Stone-Soup/blob/v1.2/docs/tutorials/01_KalmanFilterTutorial.py) |

Stone Soup is distributed under the MIT License. Its full copyright and permission notice is reproduced in [LICENSES/Stone-Soup-MIT.txt](LICENSES/Stone-Soup-MIT.txt), copied from the [official v1.2 license](https://github.com/dstl/Stone-Soup/blob/v1.2/LICENSE).

The upstream portions of the two modules correspond to Stone Soup v1.2 when blank lines and the research additions are excluded. This comparison identifies a source for the preserved notice; it does not establish the exact originally installed version or a tested dependency requirement. See the [installation guide](docs/installation.md) for compatibility limitations.

The notebook's simulation setup also includes code corresponding to the Stone Soup Kalman filter tutorial linked above, covered by the same upstream MIT notice.

Copyright in the upstream portions remains with the holders named in the Stone Soup notice. The [root MIT license](LICENSE) covers this repository's original software and documentation contributions. Redistribution of the combined code must retain the applicable copyright and permission notices, including the Stone Soup notice.

## Independent research

Mohamad Kassab conducted this research independently of the Stone Soup project and has no affiliation with it. This repository is not an official Stone Soup project and is not sponsored or endorsed by Stone Soup or its developers. Use of the library and attribution of its code do not imply a partnership or endorsement.

## Research publications and other dependencies

The [associated paper](docs/research.md) credits earlier AKKF research and related implementations. The software license does not grant rights to the separately distributed paper or full report.

Stone Soup and the other dependencies installed through the setup guide retain their own licenses. This notice does not replace the license files supplied with those packages.
