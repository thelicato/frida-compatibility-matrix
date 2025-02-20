# Frida Compatibility Matrix

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/thelicato/frida-compatibility-matrix/updater.yaml?branch=main)
![GitHub last commit](https://img.shields.io/github/last-commit/thelicato/frida-compatibility-matrix)
![License](https://img.shields.io/github/license/thelicato/frida-compatibility-matrix)


The **Frida Compatibility Matrix** provides an easy-to-read table that displays the compatible versions of the [`frida`](https://pypi.org/project/frida/) package for each version of the [`frida-tools`](https://pypi.org/project/frida-tools/) package. This is particularly useful for developers and security researchers working with Frida who need to ensure compatibility between the core Frida library and its tools.

## Why?

In many cases, security researchers need to downgrade or change the version of Frida to match specific testing environments or tools. This repository simplifies that process by mapping compatible versions, making it easier to switch between them seamlessly.

Additionally, the versioning of the `frida-tools` package follows a different scheme than `frida`, which can cause confusion. Since the `frida-server` version is aligned with `frida`, this compatibility matrix can be particularly useful in ensuring the correct versions are used together.

## Compatibility Matrix


## How it Works

The repos contains Python scripts (in the `scripts` folder) that fetch and determine compatibility between `frida` and `frida-tools`. A GitHub Workflow is set to run these scripts automatically **once a day** to keep the compatibility table up to date. The following scripts are present:

* `parser.py`: Provides utility functions to fetch and process compatibility matrix data.
* `cli.py`: A simple script that uses functions from `parser.py` to print the compatibility matrix table to stdout (mainly for testing purposes).
* `updater.py`: Script invoked by the GitHub Workflow to automatically update the README with the latest compatibility table.
* `output.py`: script invoked by the GitHub Workflow to automatically upload a JSON structured file in the `Release` section.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.