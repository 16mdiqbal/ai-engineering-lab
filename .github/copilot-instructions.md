# GitHub Copilot Instructions

## Project Overview

This is an AI Engineer course repository containing weekly Python assignments focused on data analysis, visualization, and machine learning.

---

## Core Rules & Guardrails

### 🚫 Anti-Hallucination Rules

1. **NEVER invent functions, methods, or APIs that don't exist**
   - Only suggest code using documented Python standard library features
   - Only use installed packages listed in `requirements.txt`
   - If unsure about an API, use standard, well-documented alternatives

2. **NEVER assume file paths or data structures**
   - Always check actual file structure before suggesting imports
   - Verify column names exist in datasets before using them
   - Don't assume variables exist without context

3. **NEVER generate fake data or mock implementations for production code**
   - Use actual data from provided CSV files in `resources/`
   - If sample data needed, clearly mark it as "example only"

4. **ALWAYS verify before suggesting:**
   - Package availability (check `requirements.txt`)
   - File existence (check actual project structure)
   - Method signatures (use established patterns from existing code)
   - Import paths (respect the actual module structure)

---

## Project-Specific Guidelines

### Code Organization (Follow AGENTS.md)

```python
# ✅ CORRECT: Follow project structure
from python_script.covid_analysis import CSVHandler
from python_script.plot_images import PlotImages

# ❌ WRONG: Don't invent new modules
from utils.helpers import magic_function  # Doesn't exist!
```

### Naming Conventions

```python
# ✅ CORRECT
class HousePricePrediction:           # PascalCase for classes
def calculate_prediction_interval():  # snake_case for functions
CONFIDENCE_LEVEL = 0.95               # UPPER_SNAKE for constants

# ❌ WRONG
class house_price_model:              # Wrong case
def CalculatePrice():                 # Wrong case
confidenceLevel = 0.95                # Wrong case
```

### Type Hints (Required)

```python
# ✅ CORRECT: Always include type hints
def predict_price(self, model: LinearRegression, X_new: pd.DataFrame) -> np.ndarray:
    return model.predict(X_new)

# ❌ WRONG: Missing type hints
def predict_price(self, model, X_new):
    return model.predict(X_new)
```

### Docstrings (Required for Public Methods)

```python
# ✅ CORRECT: Clear, concise docstrings
def format_prediction_output(self, predicted_price: float, square_footage: float) -> None:
    """Format and display the prediction output in a formatted box.
    
    Args:
        predicted_price: The predicted house price in dollars
        square_footage: Input square footage value
    """
    # Implementation...

# ❌ WRONG: Missing or vague docstrings
def format_output(self, price, sqft):
    # Formats stuff
    pass
```

---

## Data Science Specific Rules

### Working with DataFrames

```python
# ✅ CORRECT: Verify columns exist
if 'Square_Footage' in df.columns and 'House_Price' in df.columns:
    X = df[['Square_Footage']]
    y = df['House_Price']
else:
    raise ValueError(f"Required columns not found. Available: {df.columns.tolist()}")

# ❌ WRONG: Assume columns exist
X = df[['SquareFootage']]  # Column name might be different!
```

### Using sklearn Models

```python
# ✅ CORRECT: Use DataFrames to preserve feature names
X_new = pd.DataFrame([[square_footage]], columns=['Square_Footage'])
prediction = model.predict(X_new)

# ❌ WRONG: Use numpy arrays (causes sklearn warnings)
X_new = np.array([[square_footage]])
prediction = model.predict(X_new)
```

### Visualization

```python
# ✅ CORRECT: Use project's PlotImages class
from python_script.plot_images import PlotImages
plotter = PlotImages()
fig = plotter.plot_scatter(df, 'x_col', 'y_col')

# ❌ WRONG: Direct matplotlib without project patterns
import matplotlib.pyplot as plt
plt.scatter(df['x'], df['y'])  # Doesn't follow project style
```

---

## Testing & Validation

### Before Suggesting Code, Verify:

1. **Imports are valid:**
   ```python
   # Check requirements.txt for available packages
   # Use only: pandas, numpy, scikit-learn, matplotlib, seaborn, scipy
   ```

2. **File paths are correct:**
   ```python
   # ✅ Use Path and verify
   from pathlib import Path
   file_path = Path(__file__).resolve().parents[2] / 'resources' / 'data.csv'
   if not file_path.exists():
       raise FileNotFoundError(f"Dataset not found: {file_path}")
   ```

3. **Method signatures match existing patterns:**
   ```python
   # Look at CSVHandler, PlotImages classes for reference
   # Match their style and patterns
   ```

---

## Statistical/ML Code Rules

### Statistical Formulas

```python
# ✅ CORRECT: Include formula in comments
def calculate_prediction_interval(self, rmse: float, t_value: float, n: int) -> float:
    """Calculate prediction interval.
    
    Formula: PI = ŷ ± t * RMSE * sqrt(1 + 1/n + (x - x̄)²/(n * s²))
    
    Args:
        rmse: Root mean squared error from model
        t_value: Critical t-value for confidence level
        n: Sample size
    """
    # Implementation with formula reference
```

### Confidence Intervals

```python
# ✅ CORRECT: Use scipy.stats for statistical calculations
from scipy import stats
t_value = stats.t.ppf(0.975, n - 2)  # 95% confidence, df = n-2

# ❌ WRONG: Hardcode or invent values
t_value = 1.96  # Too simplistic, doesn't account for sample size
```

---

## User Interaction Rules

### Input Validation

```python
# ✅ CORRECT: Validate all user inputs
try:
    square_footage = float(user_input)
    if square_footage <= 0:
        print("Please enter a positive number.")
        continue
except ValueError:
    print("Invalid input. Please enter a number.")

# ❌ WRONG: No validation
square_footage = float(input("Enter sqft: "))  # Can crash!
```

### Output Formatting

```python
# ✅ CORRECT: Use consistent, clear formatting
print(f"Predicted Price: ${predicted_price:,.2f}")
print(f"Confidence Interval: ${lower:,.2f} - ${upper:,.2f}")

# ❌ WRONG: Unclear or inconsistent
print(f"Price: {predicted_price}")  # No currency symbol, no formatting
```

---

## Error Handling Rules

### Exceptions

```python
# ✅ CORRECT: Specific exceptions with helpful messages
def load_data(self, file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")
    try:
        return pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        raise ValueError(f"CSV file is empty: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to load data: {e}")

# ❌ WRONG: Bare except or generic messages
try:
    df = pd.read_csv(file_path)
except:
    print("Error!")  # Not helpful!
```

---

## Performance & Best Practices

### Avoid Unnecessary Computations

```python
# ✅ CORRECT: Cache expensive calculations
self._correlation_matrix = None

@property
def correlation_matrix(self):
    if self._correlation_matrix is None:
        self._correlation_matrix = self.df.corr()
    return self._correlation_matrix

# ❌ WRONG: Recalculate every time
def get_correlation(self):
    return self.df.corr()  # Expensive, repeated calls
```

### Memory Efficiency

```python
# ✅ CORRECT: Clean up large objects
fig = self.plot_scatter(df, 'x', 'y')
self.save_figure(fig, ax, 'output.png')
plt.close(fig)  # Free memory

# ❌ WRONG: Leave figures open
fig = plt.figure()
# ... never closed, memory leak
```

---

## Git Commit Messages (Conventional Commits)

When suggesting commits, use this format:

```bash
# ✅ CORRECT
feat: add prediction interval calculation to house price model
fix: resolve sklearn feature name warning in prediction method
refactor: extract formatting logic to separate method
docs: add docstrings to prediction methods

# ❌ WRONG
"updated files"
"fixes"
"changes"
```

---

## Guardrail Checklist for Generated Code

Before suggesting code, ensure:

- [ ] All imports are from known packages in `requirements.txt`
- [ ] All file paths use `Path` and check existence
- [ ] All DataFrame columns are validated before access
- [ ] All functions have type hints
- [ ] All public methods have docstrings
- [ ] All user inputs are validated
- [ ] All errors have helpful messages
- [ ] Code follows project naming conventions
- [ ] No magic numbers (use named constants)
- [ ] No assumed data structures (verify first)

---

## When Uncertain

If you're uncertain about:

1. **A package/module:** Check `requirements.txt` first, or use standard library
2. **A method signature:** Look at existing code in the project
3. **Data structure:** Ask for clarification or provide defensive code
4. **Best approach:** Suggest the simplest, most standard solution

### Template for Uncertain Suggestions:

```python
# NOTE: This assumes [assumption]. Please verify:
# - Column 'X' exists in your DataFrame
# - Package 'Y' is installed (add to requirements.txt if needed)
# If this doesn't match your setup, please provide more details.

def suggested_function():
    # Implementation with clear assumptions stated
    pass
```

---

## Examples of Good vs Bad Suggestions

### ❌ BAD (Hallucinated):

```python
# Don't suggest this - package doesn't exist!
from ai_utils import AutoPredictor
model = AutoPredictor.magic_fit(data)
```

### ✅ GOOD (Verified):

```python
# This uses actual scikit-learn from requirements.txt
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

### ❌ BAD (Assumed structure):

```python
# Assumes column names without verification
df['price'].mean()
```

### ✅ GOOD (Validated):

```python
# Verifies column exists
if 'price' in df.columns:
    mean_price = df['price'].mean()
else:
    raise ValueError(f"Column 'price' not found. Available: {df.columns.tolist()}")
```

---

## Summary

**Golden Rule:** Only suggest code you can verify exists or is standard practice. When in doubt, use simple, well-documented approaches from the Python standard library or verified packages in `requirements.txt`.

**Remember:** It's better to suggest slightly more verbose but verified code than concise code that might not work.

**Quality over Cleverness:** Prefer readable, maintainable code that follows project patterns over clever one-liners.

---

*Last Updated: October 26, 2025*
*Follow AGENTS.md for additional project structure and workflow guidelines*

