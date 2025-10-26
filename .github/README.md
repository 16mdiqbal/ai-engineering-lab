# GitHub Copilot Configuration

## About This File

`copilot-instructions.md` contains custom instructions for GitHub Copilot to follow when generating code suggestions for this project.

## How It Works

When you use GitHub Copilot in this repository, it will automatically:
- ✅ Follow project-specific coding standards
- ✅ Use verified packages from `requirements.txt`
- ✅ Respect the project structure defined in `AGENTS.md`
- ✅ Apply anti-hallucination guardrails
- ✅ Include proper type hints and docstrings
- ✅ Validate data structures before use

## Key Guardrails

### Anti-Hallucination
- Won't suggest packages that don't exist
- Won't assume DataFrame columns without verification
- Won't invent APIs or methods

### Code Quality
- Always includes type hints
- Adds docstrings for public methods
- Validates user inputs
- Uses proper error handling

### Project Standards
- Follows naming conventions (snake_case, PascalCase)
- Matches existing code patterns
- Uses Conventional Commit messages

## Usage

Just code normally! Copilot will:
1. Read these instructions automatically
2. Apply them to all suggestions
3. Generate code that follows project standards

## Updating Instructions

To modify Copilot's behavior:
1. Edit `copilot-instructions.md`
2. Commit the changes
3. Copilot will use the updated rules immediately

---

**Note:** These instructions help Copilot generate better code, but always review suggestions before accepting them!

