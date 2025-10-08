# AI Engineer Exercise — Highlights

- Data file: put the dataset at `resources/country_wise_latest.csv`.
- Outputs:
  - Week 4: CSV at `week4-assignment/assignment/country_wise_sorted.csv`.
  - Week 5: plots under `week5-assignment/plot_images/`.
- Imports: the reusable code lives in the `python_script` package; it’s a namespace package (no `__init__.py` needed). After editable install, import with:
  `from python_script.covid_analysis.DataAnalyser import DataAnalyzer`.

## Quick setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Run
- Week 4 analysis (prints results, writes sorted CSV):
```bash
python week4-assignment/python/CoronaDataAnalysis.py
```
- Week 5 visualizations (saves figures):
```bash
python week5-assignment/python/DataVisualisationAndEDA.py
```

## Clean up (optional)
```bash
make clean-pyc
rm -rf week5-assignment/plot_images/
```

## Troubleshooting
- If you see `ModuleNotFoundError`, ensure the venv is active and you ran `pip install -e .`.
- If data isn’t found, verify `resources/country_wise_latest.csv` exists.
