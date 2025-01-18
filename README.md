
![demo](https://github.com/user-attachments/assets/62ca9c47-e35a-4c2e-bbc0-0d19ee8b4df3)

[![GitHub Repo](https://img.shields.io/github/stars/mpruvot/CommitCrafter?style=social)](https://github.com/mpruvot/CommitCrafter)
[![GitHub Issues](https://img.shields.io/github/issues/mpruvot/CommitCrafter)](https://github.com/mpruvot/CommitCrafter/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/mpruvot/CommitCrafter)](https://github.com/mpruvot/CommitCrafter/pulls)

# CommitCrafter 🎨

Craft your commit messages while you focus on coding. CommitCrafter analyzes your git diff and generates meaningful, conventional commit messages.

## ✨ What's Cool

- 🤖 **Multiple AI Brains**: Choose your favorite - GPT, Claude, Gemini, Mistral, or Ollama
- 🎯 **Smart Selection**: Pick from multiple suggestions for the perfect commit message  
- 📋 **Auto-Copy**: Selected message goes straight to your clipboard
- 🎭 **Conventional Commits**: Proper formatting with emojis included
- 🔌 **Just Works**: Zero config needed - works with any git repo

## 🚀 Quick Start

```bash
# Install with pipx
pipx install commitcrafter

# Use it (in any git repository)
commitcraft         # Uses Claude by default
commitcraft -a gpt  # Or use GPT instead
```

## 🎮 Choose Your Model

```bash
commitcraft -a claude   # Anthropic's Claude
commitcraft -a gpt      # OpenAI's GPT
commitcraft -a gemini   # Google's Gemini
commitcraft -a mistral  # Mistral AI
commitcraft -a ollama   # Local Ollama
```

## 🔑 Setup

You'll need an API key for your chosen model. Set it as an environment variable:

```bash
# Pick the one you need:
export ANTHROPIC_API_KEY='your-key'
export OPENAI_API_KEY='your-key'
export GEMINI_API_KEY='your-key'
export MISTRAL_API_KEY='your-key'
export OLLAMA_API_KEY='your-key'
```

## 📦 Requirements

- Python 3.12+
- A git repository
- An API key for your chosen model

## 🤝 Contributing

Found a bug? Have an idea? PRs and issues are always welcome!

## 📝 License

MIT - Do whatever you want with it!

## 🔗 Useful Links

### 🛠️ Built With
- [Pydantic-AI](https://github.com/pydantic/pydantic-ai) - Modern AI Agent Framework
- [Typer](https://typer.tiangolo.com/) - Beautiful CLI Builder
- [Rich](https://github.com/Textualize/rich) - Rich Terminal Output
- [GitPython](https://github.com/gitpython-developers/GitPython) - Git Operations
- [Pyperclip](https://github.com/asweigart/pyperclip) - Clipboard Management

### 🤖 AI Providers
- [Anthropic Claude](https://www.anthropic.com/) - Our Default Model
- [OpenAI](https://openai.com/) - GPT Integration
- [Google Gemini](https://gemini.google.com/) - Google's LLM
- [Mistral AI](https://mistral.ai/) - Open Source Models
- [Ollama](https://github.com/jmorganca/ollama) - Local AI Runtime

