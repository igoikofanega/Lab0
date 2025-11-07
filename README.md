# Lab0 - Continuous Integration Fundamentals

## Comandos

```bash
# Linting
uv run python -m pylint src/*.py

# Formateo
uv run black src/*.py

# Tests
uv run python -m pytest -v

# Cobertura
uv run python -m pytest -v --cov=src