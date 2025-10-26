# GitHub Actions - Quick Syntax Check

## 🎯 What It Does

This workflow runs on every Pull Request and checks for **Python syntax errors only**.

**What it checks:**
- ✅ Python syntax errors (missing parenthesis, invalid code)
- ✅ Compilation issues (code that won't run)

**What it does NOT check:**
- ❌ Code style or formatting
- ❌ Line length or spacing
- ❌ Import order
- ❌ Code quality

---

## 🚀 How to Use

### Before Creating a PR:

```bash
# Quick syntax check (optional)
python -m py_compile your_file.py
```

### When PR is Created:
- Workflow runs automatically
- Takes ~30 seconds
- Only fails if code has syntax errors

---

## 🔧 Files Needed

### Required (DO NOT MOVE):
- `.github/workflows/lint.yml` - The workflow
- `.github/PULL_REQUEST_TEMPLATE.md` - PR template

### Not Needed:
- No config files required
- No linting tools needed

---

## 💻 Test Locally

```bash
# Check all Python files
find . -name "*.py" ! -path "./.venv*/*" -exec python -m py_compile {} +

# No output = all good ✅
```

---

## ❌ Troubleshooting

**If the check fails:**
1. Look at the error message
2. Find the file and line number
3. Fix the syntax error
4. Push again

**Example error:**
```
SyntaxError: invalid syntax (week7-assignment/python/file.py, line 42)
```

**Fix:** Go to that file, line 42, and fix the syntax error.

---

## 📝 That's It!

Simple, fast, no unnecessary checks. Just make sure your code compiles! ✅

