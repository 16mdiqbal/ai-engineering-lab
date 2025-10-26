# Project Documentation

This directory contains documentation for various aspects of the project.

## 📂 Documentation Sections

### [GitHub Actions](github-actions/)
CI/CD workflow documentation, setup guides, and troubleshooting.

- [Setup Summary](github-actions/SETUP_SUMMARY.md) - How to set up GitHub Actions
- [Workflow Guide](github-actions/README.md) - Details about the lint workflow
- [Troubleshooting](github-actions/FLAKE8_FIX.md) - Common issues and fixes

## 🚀 Quick Links

### GitHub Actions
- **Workflow Status:** Check the "Actions" tab on GitHub
- **Configuration Files:** `.flake8`, `pyproject.toml` in project root
- **Test Locally:** Run `docs/github-actions/test-flake8-config.sh`

### Project Structure
```
ai-engineer-exercise/
├── .github/                    # GitHub configuration (REQUIRED for workflows)
│   ├── workflows/
│   │   └── lint.yml           # ← GitHub Actions workflow (DO NOT MOVE)
│   └── PULL_REQUEST_TEMPLATE.md  # ← PR template (REQUIRED for GitHub)
├── docs/                       # Documentation (can be moved/organized freely)
│   └── github-actions/         # GitHub Actions documentation
├── .flake8                     # Flake8 config (REQUIRED in root)
├── pyproject.toml              # Black/isort config (REQUIRED in root)
└── ...
```

## 📋 What Files Must Stay in `.github/`?

### ✅ Required in `.github/` (GitHub looks for these):
- `.github/workflows/*.yml` - Workflow definitions
- `.github/PULL_REQUEST_TEMPLATE.md` - PR template

### 📄 Optional (can be anywhere):
- Documentation (`.md` files) - Moved to `docs/`
- Test scripts - Moved to `docs/`
- README files - Moved to `docs/`

## 🔍 Finding Documentation

All documentation is now organized in the `docs/` directory by topic. Check the subdirectories for specific guides.

