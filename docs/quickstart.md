# Quick Start Guide 🚀

Get up and running with CommitCrafter in minutes.

## Installation

```bash
# Using pipx (recommended)
pipx install commitcrafter

# Or using pip
pip install commitcrafter
```

## First Steps

1. **Navigate to your git repository**
```bash
cd your-project
```

2. **Make and stage some changes**
```bash
# Make your changes
git add .
```

3. **Generate a commit message**
```bash
commitcraft
```

4. **Select from the suggestions and you're done!**

## Real-World Examples

### Adding a Feature
```bash
$ git add src/auth.py
$ commitcraft
# Suggestions:
# 1. ✨ feat: add user authentication system
# 2. ✨ feat: implement basic auth functionality
# 3. ✨ feat: create authentication module
```

### Fixing a Bug
```bash
$ git add src/memory.py
$ commitcraft
# Suggestions:
# 1. 🐛 fix: resolve memory leak in data processing
# 2. 🐛 fix: prevent memory overflow in large datasets
# 3. 🐛 fix: address memory management issue
```

[Configure API Keys →](configuration.md){ .md-button .md-button--primary }