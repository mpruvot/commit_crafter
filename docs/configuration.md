# Configuration Guide ⚙️

## Setting Up API Keys

### Claude (Default Choice)
1. Create an account at [Anthropic Console](https://console.anthropic.com/)
2. Generate your API key
3. Set it in your environment:
```bash
export ANTHROPIC_API_KEY='your-key'
```

### Other Providers

=== "OpenAI GPT"
    ```bash
    export OPENAI_API_KEY='your-key'
    ```

=== "Google Gemini"
    ```bash
    export GEMINI_API_KEY='your-key'
    ```

=== "Mistral"
    ```bash
    export MISTRAL_API_KEY='your-key'
    ```

=== "Ollama"
    ```bash
    export OLLAMA_API_KEY='your-key'
    ```

## Commit Types Guide

CommitCrafter uses conventional commits with emojis:

| Emoji | Type | Use Case |
|-------|------|----------|
| ✨ | `feat` | New features |
| 🐛 | `fix` | Bug fixes |
| 📚 | `docs` | Documentation |
| 💄 | `style` | Code style updates |
| ♻️ | `refactor` | Code refactoring |
| ⚡️ | `perf` | Performance |
| 🧪 | `test` | Testing |
| 🔧 | `chore` | Maintenance |

[Explore Models →](models/index.md){ .md-button .md-button--primary }
