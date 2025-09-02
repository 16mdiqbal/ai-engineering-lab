# Repository Guidelines

## Project Structure & Module Organization
- Root contains `ai-engineer-assignment/` where all coursework lives.
- Organize by week or topic: `ai-engineer-assignment/<week-or-topic>/` (e.g., `week1-assignment/`).
- Each folder can hold standalone scripts and notebooks. A structure like `src/`, `notebooks/`, `assets/`, and `data/` is optional—use it when the code grows.
  - Use two-digit numbering for assignments: `01_topic.py`, `02_topic.py` inside a subfolder like `python/`. Example: `ai-engineer-assignment/week1-assignment/python/01_fizzbuzz.py`.

## Build, Test, and Development Commands
- Create env: `python -m venv .venv && source .venv/bin/activate`.
- Install deps (if present): `pip install -r requirements.txt`.
- Run a script directly: `python ai-engineer-assignment/<folder>/<script>.py`.
- Using Makefile (from repo root): `make run W=week1-assignment S=python/01_fizzbuzz.py`.
- Optional modules: if you add packages later, use `python -m <package_or_module>`.

## Coding Style & Naming Conventions
- Python, 4‑space indent; add type hints and short docstrings for public functions.
- Files and functions: `snake_case`; classes: `PascalCase`; constants: `UPPER_SNAKE`.
- Assignment scripts: prefix with two digits reflecting order (e.g., `01_fizzbuzz.py`, `02_password_retry.py`).
- Notebooks: `lowercase-with-dashes.ipynb`; keep heavy logic in importable `.py` files when it helps reuse.
- Formatters/linters (optional): `black .`, `ruff .`, `mypy .`.

## Testing Guidelines
- No default test framework configured. When needed, add simple self-check scripts or adopt `pytest`.
- If adopting `pytest`, mirror code with a `tests/` folder (e.g., `weekN/tests/test_example.py`) and run `pytest -q`.

## Commit & Pull Request Guidelines
- Use Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`, etc.
- Keep commits focused and readable; include rationale in the body when non‑obvious.
- PRs: clear description, scope, linked issue/task, and usage notes or sample output. Screenshots help for notebook visuals.
- Prefer small PRs (≤300 lines diff). Ensure scripts run locally.

## Security & Configuration Tips
- Never commit secrets. Use environment variables (`.env*` are ignored) and document required keys in the week/topic `README.md`.
- Place large datasets in `data/` and keep them out of Git; include brief download notes when relevant.

## Agent-Specific Instructions
- If using AI assistants, note generated files in your PR and summarize any manual edits. Ensure outputs follow the style, tests pass, and code is reproducible end‑to‑end.
