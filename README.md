Cookiecutter template for starting a flake8 plugin project.

## Requirements

```
pip install cookiecutter
```

## Usage

```
cookiecutter https://github.com/sondrelg/cookiecutter-flake8-plugin
```

## What's included, outside the plugin

- [poetry](https://python-poetry.org/) for dependency management
- [github action](https://docs.github.com/en/actions) for running linting and tests in your (assumed) github repository
- [pre-commit](https://github.com/pre-commit/pre-commit) with 
  - [flake8](https://github.com/PyCQA/flake8)
  - [mypy](https://github.com/python/mypy)
  - [isort](https://github.com/PyCQA/isort)
    
  for linting and code quality checking
    
