# pre-commit-demo
This is a demo repository that demonstrates how to integrate pre-commit in a project consisting of various files including text, yaml, python, javascript, css, and html.

## Prerequisites
- [pre-commit](https://pre-commit.com/)
- [Git](https://git-scm.com/)

## Setup

1. Clone the repository: 
```
git clone https://github.com/sameeramin/pre-commit-demo.git
```
2. Install pre-commit: 
```
brew install pre-commit
```
Or
```
pip install pre-commit
```
Or if you're using `anaconda` or `miniconda`
```
conda install pre-commit
```
3. Run `pre-commit install` to install the git hook

4. Make your changes and commit. You will see pre-commit running the hooks automatically. If you want to run it on existing files run 
```
pre-commit run --all-files  
```

## Available Hooks
- `check-yaml`: checks yaml file for proper formatting
- `end-of-file-fixer`: checks for newline at end of files
- `trailing-whitespace`: checks for whitespaces at the end of lines
- `black`: auto-formats python code to conform to PEP8 style
- `flake8`: checks for code style and errors

You can add more hooks as per your project requirements. Here's the [list](https://pre-commit.com/hooks.html) of all supported hooks and you can also create your own hooks as well!

## Note
Make sure you have all the necessary dependencies installed before running the pre-commit hooks

You can add or remove hooks in the `.pre-commit-config.yaml` file

## Support
If you have any issues or questions, please open an issue on the repository and I'll be happy to help. If this guide helped you, please consider staring this repository 😂
