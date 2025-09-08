# Week 1 Assignment

This folder contains Python practice scripts for Week 1. Files use a two‑digit prefix to indicate assignment order.

## Structure
- `python/01_fizzbuzz.py`: Print numbers 1..N with Fizz/Buzz rules.
- `python/02_password_retry.py`: Prompt for a password with limited retries.
- `html/`: Any writeups or notes exported as HTML.

## Run Scripts
From the repository root:
- Using Python directly: `python ai-engineer-assignment/week1-assignment/python/01_fizzbuzz.py`
- Using Makefile: `make run W=week1-assignment S=python/01_fizzbuzz.py`

Tip: Create and use a virtual env first:
`python -m venv .venv && source .venv/bin/activate`

## Conventions
- Filenames: `NN_topic.py` where `NN` is `01`, `02`, ...
- Keep scripts self‑contained and simple. Add dependencies to `requirements.txt` if needed.
