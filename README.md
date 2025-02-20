# Frida Compatibility Matrix

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/thelicato/frida-compatibility-matrix/updater.yaml?branch=main)
![GitHub last commit](https://img.shields.io/github/last-commit/thelicato/frida-compatibility-matrix)
![License](https://img.shields.io/github/license/thelicato/frida-compatibility-matrix)


The **Frida Compatibility Matrix** provides an easy-to-read table that displays the compatible versions of the [`frida`](https://pypi.org/project/frida/) package for each version of the [`frida-tools`](https://pypi.org/project/frida-tools/) package. This is particularly useful for developers and security researchers working with Frida who need to ensure compatibility between the core Frida library and its tools.

## Why?

In many cases, security researchers need to downgrade or change the version of Frida to match specific testing environments or tools. This repository simplifies that process by mapping compatible versions, making it easier to switch between them seamlessly.

Additionally, the versioning of the `frida-tools` package follows a different scheme than `frida`, which can cause confusion. Since the `frida-server` version is aligned with `frida`, this compatibility matrix can be particularly useful in ensuring the correct versions are used together.

## Compatibility Matrix

| `frida-tools` | `frida`              |
| ------------- | -------------------- |
| 13.6.1        | >= 16.2.2, < 17.0.0  |
| 13.6.0        | >= 16.2.2, < 17.0.0  |
| 13.5.0        | >= 16.2.2, < 17.0.0  |
| 13.4.0        | >= 16.2.2, < 17.0.0  |
| 13.3.0        | >= 16.2.2, < 17.0.0  |
| 13.2.1        | >= 16.2.2, < 17.0.0  |
| 13.2.0        | >= 16.2.2, < 17.0.0  |
| 13.1.0        | >= 16.2.2, < 17.0.0  |
| 13.0.4        | >= 16.2.2, < 17.0.0  |
| 13.0.3        | >= 16.2.2, < 17.0.0  |
| 13.0.2        | >= 16.2.2, < 17.0.0  |
| 13.0.1        | >= 16.2.2, < 17.0.0  |
| 13.0.0        | >= 16.2.2, < 17.0.0  |
| 12.5.1        | >= 16.2.2, < 17.0.0  |
| 12.5.0        | >= 16.2.2, < 17.0.0  |
| 12.4.4        | >= 16.2.2, < 17.0.0  |
| 12.4.3        | >= 16.2.2, < 17.0.0  |
| 12.4.2        | >= 16.2.2, < 17.0.0  |
| 12.4.1        | >= 16.2.2, < 17.0.0  |
| 12.4.0        | >= 16.2.2, < 17.0.0  |
| 12.3.0        | >= 16.0.9, < 17.0.0  |
| 12.2.1        | >= 16.0.9, < 17.0.0  |
| 12.2.0        | >= 16.0.9, < 17.0.0  |
| 12.1.3        | >= 16.0.9, < 17.0.0  |
| 12.1.2        | >= 16.0.9, < 17.0.0  |
| 12.1.1        | >= 16.0.9, < 17.0.0  |
| 12.1.0        | >= 16.0.0, < 17.0.0  |
| 12.0.4        | >= 16.0.0, < 17.0.0  |
| 12.0.3        | >= 16.0.0, < 17.0.0  |
| 12.0.2        | >= 16.0.0, < 17.0.0  |
| 12.0.1        | >= 16.0.0, < 17.0.0  |
| 12.0.0        | >= 16.0.0, < 17.0.0  |
| 11.0.0        | >= 15.2.0, < 16.0.0  |
| 10.8.0        | >= 15.0.0, < 16.0.0  |
| 10.7.0        | >= 15.0.0, < 16.0.0  |
| 10.6.2        | >= 15.0.0, < 16.0.0  |
| 10.6.1        | >= 15.0.0, < 16.0.0  |
| 10.6.0        | >= 15.0.0, < 16.0.0  |
| 10.5.4        | >= 15.0.0, < 16.0.0  |
| 10.5.3        | >= 15.0.0, < 16.0.0  |
| 10.5.2        | >= 15.0.0, < 16.0.0  |
| 10.5.1        | >= 15.0.0, < 16.0.0  |
| 10.5.0        | >= 15.0.0, < 16.0.0  |
| 10.4.1        | >= 15.0.0, < 16.0.0  |
| 10.4.0        | >= 15.0.0, < 16.0.0  |
| 10.3.0        | >= 15.0.0, < 16.0.0  |
| 10.2.2        | >= 15.0.0, < 16.0.0  |
| 10.2.1        | >= 15.0.0, < 16.0.0  |
| 10.2.0        | >= 15.0.0, < 16.0.0  |
| 10.1.1        | >= 15.0.0, < 16.0.0  |
| 10.1.0        | >= 15.0.0, < 16.0.0  |
| 10.0.0        | >= 15.0.0, < 16.0.0  |
| 9.2.5         | >= 14.2.9, < 15.0.0  |
| 9.2.4         | >= 14.2.9, < 15.0.0  |
| 9.2.3         | >= 14.2.9, < 15.0.0  |
| 9.2.2         | >= 14.2.9, < 15.0.0  |
| 9.2.1         | >= 14.2.9, < 15.0.0  |
| 9.2.0         | >= 14.2.9, < 15.0.0  |
| 9.1.0         | >= 14.2.0, < 15.0.0  |
| 9.0.1         | >= 14.0.0, < 15.0.0  |
| 9.0.0         | >= 14.0.0, < 15.0.0  |
| 8.2.0         | >= 12.10.4, < 13.0.0 |
| 8.1.3         | >= 12.10.4, < 13.0.0 |
| 8.1.2         | >= 12.10.4, < 13.0.0 |
| 8.1.1         | >= 12.10.4, < 13.0.0 |
| 8.1.0         | >= 12.10.4, < 13.0.0 |
| 8.0.1         | >= 12.10.4, < 13.0.0 |
| 8.0.0         | >= 12.10.4, < 13.0.0 |
| 7.2.2         | >= 12.8.12, < 13.0.0 |
| 7.2.1         | >= 12.8.12, < 13.0.0 |
| 7.2.0         | >= 12.8.12, < 13.0.0 |
| 7.1.0         | >= 12.8.12, < 13.0.0 |
| 7.0.2         | >= 12.8.12, < 13.0.0 |
| 7.0.1         | >= 12.8.12, < 13.0.0 |
| 7.0.0         | >= 12.8.12, < 13.0.0 |
| 6.0.1         | >= 12.8.5, < 13.0.0  |
| 6.0.0         | >= 12.8.5, < 13.0.0  |
| 5.4.0         | >= 12.7.3, < 13.0.0  |
| 5.3.0         | >= 12.7.3, < 13.0.0  |
| 5.2.0         | >= 12.7.3, < 13.0.0  |
| 5.1.0         | >= 12.7.3, < 13.0.0  |
| 5.0.1         | >= 12.7.3, < 13.0.0  |
| 5.0.0         | >= 12.6.21, < 13.0.0 |
| 4.1.0         | >= 12.6.21, < 13.0.0 |
| 4.0.2         | >= 12.6.21, < 13.0.0 |
| 4.0.1         | >= 12.6.21, < 13.0.0 |
| 4.0.0         | >= 12.6.21, < 13.0.0 |
| 3.0.1         | >= 12.6.17, < 13.0.0 |
| 3.0.0         | >= 12.6.17, < 13.0.0 |
| 2.2.0         | >= 12.5.9, < 13.0.0  |
| 2.1.1         | >= 12.5.9, < 13.0.0  |
| 2.1.0         | >= 12.5.9, < 13.0.0  |
| 2.0.2         | >= 12.5.9, < 13.0.0  |
| 2.0.1         | >= 12.5.9, < 13.0.0  |
| 2.0.0         | >= 12.5.3, < 13.0.0  |
| 1.3.2         | >= 12.4.0, < 13.0.0  |
| 1.3.1         | >= 12.3.0, < 13.0.0  |
| 1.3.0         | >= 12.3.0, < 13.0.0  |
| 1.2.3         | >= 12.1.0, < 13.0.0  |
| 1.2.2         | >= 12.1.0, < 13.0.0  |
| 1.2.1         | >= 12.1.0, < 13.0.0  |
| 1.2.0         | >= 12.1.0, < 13.0.0  |
| 1.1.0         | >= 12.0.0, < 13.0.0  |
| 1.0.0         | >= 12.0.0, < 13.0.0  |

## How it Works

The repos contains Python scripts (in the `scripts` folder) that fetch and determine compatibility between `frida` and `frida-tools`. A GitHub Workflow is set to run these scripts automatically **once a day** to keep the compatibility table up to date. The following scripts are present:

* `parser.py`: Provides utility functions to fetch and process compatibility matrix data.
* `cli.py`: A simple script that uses functions from `parser.py` to print the compatibility matrix table to stdout (mainly for testing purposes).
* `updater.py`: The script invoked by the GitHub Workflow to automatically update the README with the latest compatibility table.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.