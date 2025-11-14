# Lab0: Fundamentals of Continuous Integration (CI)

This project introduces the **core principles of Continuous Integration (CI)** within the MLOps workflow. It implements essential practices such as code linting, automated formatting, and comprehensive testing to ensure code quality, reliability, and maintainability.

The main application is a **Command-Line Interface (CLI)** designed to run various data preprocessing operations.

---

## Project Structure and Setup

The project adheres to MLOps best practices by using an isolated virtual environment. The final layout includes source code (`src`), test suites (`tests`), and essential configuration files.

### 1. File Structure

| Directory/File       | Description |
|----------------------|-------------|
| `pyproject.toml`     | Main project configuration file. |
| `pytest.ini`         | Pytest-specific settings. |
| `README.md`          | Project documentation and overview. |
| `src/`               | Contains the core logic and CLI implementation. |
| `src/cli.py`         | CLI implementation using the `click` library. |
| `src/__init__.py`    | Marks `src` as a Python package. |
| `src/preprocessing.py` | Core data preprocessing logic and functions. |
| `tests/`             | Directory for all test files. |
| `tests/test_cli.py`  | Integration tests between CLI and core logic. |
| `tests/test_logic.py`| Unit tests for the main preprocessing functionalities. |
| `uv.lock`            | Dependency lock file for reproducible environments. |

### 2. Dependencies

The project uses a dedicated virtual environment managed with `uv`. Dependencies are installed via `uv init` and `uv sync`:

- **`click`** – Builds the interactive Command-Line Interface.
- **`black`** – Enforces consistent code style through automatic formatting.
- **`pylint`** – Performs static analysis to detect errors and improve code quality.
- **`pytest`** – Testing framework for both unit and integration tests.
- **`pytest-cov`** – Measures test coverage across the codebase.

---

## Running the CI Pipeline

Execute the following commands from the **project root** to run CI tools.

### 1. Code Linting (Quality Assurance)

Pylint analyzes code for errors, enforces standards, detects smells, and suggests improvements. Run it with:

```bash
uv run python -m pylint src/*.py
```

### 2. Code Formatting (Style Consistency)
Use black to automatically format code according to PEP 8 standards:
```bash
uv run black src/*.py
```
### 3. Testing and Coverage
Test files and functions must follow the test_ naming convention.
# Run all tests (unit + integration)
```bash
uv run python -m pytest -v
```
# Run tests with coverage report
```bash
uv run python -m pytest -v --cov=src
```
### About
Repository for Lab0 of the MLOps course in the Machine Learning Master's program.

© 2025 GitHub, Inc.