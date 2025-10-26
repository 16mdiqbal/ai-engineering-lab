# GitHub Workflows

This directory contains GitHub Actions workflows for automated CI/CD processes.

## Workflows

### Lint Check (`lint.yml`)

**Trigger:** Runs on every pull request and push to `main`, `master`, or `develop` branches.

**Purpose:** Ensures code quality and consistency by running multiple linting tools.

**Checks performed:**
- **flake8**: Python syntax errors, undefined names, and PEP 8 violations
- **pylint**: Code quality analysis and best practices
- **black**: Code formatting consistency
- **isort**: Import statement organization

**How to run locally:**

```bash
# Install linting tools
pip install flake8 pylint black isort

# Run flake8 (syntax and style check)
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Run pylint (code quality)
pylint **/*.py

# Check formatting with black
black --check .

# Check import sorting
isort --check-only .
```

**Fix issues automatically:**

```bash
# Auto-format code with black
black .

# Auto-sort imports
isort .
```

## Configuration

The workflow uses:
- Python 3.12
- Caching for faster builds
- Continues on pylint errors (informational only)
- Fails on critical syntax errors

## Contributing

Before submitting a PR, ensure:
1. All lint checks pass locally
2. Code is formatted with `black`
3. Imports are sorted with `isort`
4. No critical flake8 errors exist

