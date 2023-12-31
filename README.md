# Advent of Code 2023 README

Advent of Code 2023 daily programming challenge, christmas themed. Website [here](https://adventofcode.com/).

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![Flake8 Status](./reports/badges/flake8-badge.svg)](./reports/flake8/index.html)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Tests Status](./reports/badges/junit-tests-badge.svg)](./reports/junit/html-test-report.html)
![Coverage](./reports/badges/cov-badge.svg)

## Version

Current version is 0.1.0 and was set according to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Project's version should be updated, when applicable:

- In this very file.
- In the changelog.
- In the \_\_init\_\_.py file inside aoc2023
- In the pyproject.toml file.

## Prerequisites

- [Poetry](https://github.com/python-poetry/poetry)
- [Pyenv](https://github.com/pyenv/pyenv)

## Documentation

In order to generate documentation, simply run:

```bash
poetry run pdoc -o docs -d google aoc2023
```

## Installation

In order to install the project, simply run:

```bash
poetry install
```

## Building

In order to generate a .whl file to distribute the project, simply run:

```bash
poetry build
```

## Testing

In order to run project tests, simply run:

```bash
poetry run pytest tests --doctest-modules
```

In order to generate XML and HTML reports, run this instead:

```bash
poetry run pytest tests --doctest-modules --junit-xml=reports/junit/junit-test-report.xml --html=reports/junit/html-test-report.html
```

## Execution

To run each day problems, it is needed to provide the adequate input file. For example, for day one:

```bash
aoc2023 day1 data/inputs/input_d1.txt
```

In order to execute the **second part** of a day's problem, the *-p* flag can be used:

```bash
aoc2023 day1 data/inputs/input_d1.txt -p 2
```

Help on the executable can be found using -h/--help flag.

## Badges generation

To generate project badges, simply ## Building

- **Unit Tests**

```bash
genbadge tests -i reports/junit/junit-test-report.xml -o reports/badges/junit-tests-badge.svg
```

- **Flake8**

```bash
genbadge flake8 -i reports/flake8/flake8stats.txt -o reports/badges/flake8-badge.svg
```

- **Code Coverage**

```bash
genbadge coverage -i reports/coverage/cov.xml -o reports/badges/cov-badge.svg
```

An utility script, called *gen-badges.sh* has been provided in order to generate them.

## License

See license file for more information.

## Authors

- [Andrés Ferreiro González](andresoferreiro@gmail.com)

## Maintainer

- [Andrés Ferreiro González](andresoferreiro@gmail.com)
