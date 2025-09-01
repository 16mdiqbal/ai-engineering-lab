# ai-engineer-assignment

Practice space for AI Engineer coursework and Python exercises.

## Layout
- Organize work by week or topic: `ai-engineer-assignment/<folder>/` (e.g., `week1-assignment/`).
- Each folder can contain standalone Python scripts and/or notebooks. No default testing setup is required.

## Getting Started
1. Create a virtual environment:
   - `python -m venv .venv && source .venv/bin/activate`
2. (Optional) Install dependencies if you add a `requirements.txt`:
   - `pip install -r requirements.txt`
3. Run a script:
   - `python ai-engineer-assignment/<folder>/<script>.py`

## Notes
- Secrets should not be committed. Use environment variables (files like `.env.local` are ignored by Git).
- Large or raw datasets belong in a `data/` subfolder which is already gitignored.
