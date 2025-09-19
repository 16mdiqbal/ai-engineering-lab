# Repository Guidelines

## Project Structure & Module Organization
- All coursework lives in `ai-engineer-assignment/`, grouped by weeks such as `ai-engineer-assignment/week1-assignment/`.
- Root folders like `week1-assignment/` remain for now; migrate them under `ai-engineer-assignment/` whenever you touch their contents to keep the layout consistent.
- Within each week, separate solution types (`python/`, `assignment/`, `html/`) and add `src/`, `notebooks/`, or `data/` only when reuse demands it.
- Name runnable scripts with two-digit prefixes (`python/01_fizzbuzz.py`, `python/02_password_retry.py`) and keep notebooks lightweight (`notebooks/progress-notes.ipynb`).
- Document dataset sources in the owning week’s `README.md`, and stash raw assets in `data/` or `assets/` folders that stay out of Git history.

## Build, Test, and Development Commands
- Bootstrap an isolated environment: `python -m venv .venv && source .venv/bin/activate` (or `make venv`).
- Install shared dependencies: `pip install -r requirements.txt` or `make install` for a scripted flow; run `make freeze` after pinning new packages.
- Execute scripts directly (`python ai-engineer-assignment/week2-assignment/python/03_data_cleanup.py`) or via Make: `make run W=week1-assignment S=python/01_fizzbuzz.py`.
- When modules evolve, prefer module invocation (`python -m ai-engineer-assignment.week1-assignment.python.01_fizzbuzz`) so relative imports behave.

## Coding Style & Naming Conventions
- Python uses 4-space indents, `snake_case` for functions/files, `PascalCase` for classes, and `UPPER_SNAKE` for constants.
- Add type hints and concise docstrings for public functions; keep notebooks thin and move reusable logic into importable modules.
- Optional tooling: `black .` for formatting, `ruff .` for linting, and `mypy .` to validate typing once modules stabilize.

## Testing Guidelines
- No default harness exists; adopt `pytest` when logic extends beyond scripts. Mirror code layout (`ai-engineer-assignment/weekN-assignment/tests/test_example.py`).
- Run suites with `pytest -q` and record coverage expectations or required fixtures in the week README so others can reproduce results.

## Commit & Pull Request Guidelines
- Follow Conventional Commits (`feat: add atm withdrawal logic`, `fix: handle zero balance`) and keep patches focused and reversible.
- PRs should summarize intent, link related lessons or issues, list validation commands (`make run ...`, `pytest -q`), and add screenshots for UI/notebook output when helpful.
- Favor small diffs (≤300 lines) and call out follow-up tasks if you defer cleanups.

## Security & Configuration Tips
- Never commit credentials or personal data. Use environment variables (`.env*` are ignored) and note required keys in the relevant README.
- Store large datasets outside Git; provide download locations and integrity checks.
- If you rely on AI tools, note generated artifacts in your PR and double-check that the outputs are reproducible end-to-end.
