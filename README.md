![ezgif-4-30ae1a8a0a](https://github.com/mpruvot/CommitCrafter/assets/132161864/ced77a15-5f3b-4e31-9011-26fcbcdfc0ad)

# CommitCrafter

**CommitCrafter** is an AI-powered tool designed to enhance Git workflows by generating descriptive commit messages based on changes made within the repository. Using either OpenAI's GPT or Anthropic's Claude APIs, it provides a seamless way to create meaningful commit messages that accurately reflect the content of your updates.

## What's New in 0.2.0 🎉

- **New AI Provider**: Added support for Claude AI through Anthropic's API
- **Interactive Selection**: Choose from multiple generated commit messages
- **Clipboard Integration**: Selected commit messages are automatically copied
- **Conventional Commits**: Added emoji support for different types of commits
- **Command Options**: New `--client` flag to switch between GPT and Claude

## Features

- **Multiple AI Providers**: Choose between GPT and Claude AI models for generating commit messages
- **Interactive Selection**: Select from multiple generated commit messages with an easy-to-use interface
- **Clipboard Integration**: Automatically copy selected commit messages to your clipboard
- **Conventional Commits**: Follows conventional commit format with appropriate emojis
- **Easy Integration**: Directly integrates with your Git repositories to analyze recent diffs
- **Customization Options**: Modify the AI prompts to better match your project's context and coding conventions

## Installation

CommitCrafter requires Python 3.12 or newer. Install CommitCrafter globally with pipx to ensure it is available in any of your projects:

```bash
pipx install commitcrafter
```

## Updating

To update to the latest version:

```bash
pipx upgrade commitcrafter
```

## Usage

To use CommitCrafter, navigate to your project directory and execute:

```bash
# Use GPT (default)
commitcraft

# Use Claude
commitcraft --client claude
# or
commitcraft -c claude
```

### Environment Setup

#### For OpenAI (GPT):
```bash
export COMMITCRAFT_OPENAI_API_KEY='your-api-key'
```

#### For Anthropic (Claude):
```bash
export ANTHROPIC_API_KEY='your-api-key'
```

Note: While OpenAI offers free credits for new users, Claude is a paid service that requires purchasing credits from Anthropic. Make sure you have sufficient credits before using the Claude integration. You can manage your Claude credits at console.anthropic.com.

## Dependencies

- Python (>=3.12)
- GitPython for repository interaction
- Typer for command-line interfaces
- Rich for formatting terminal outputs
- Pyperclip for clipboard functionality
- OpenAI and Anthropic libraries for AI integration

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues if you have suggestions for improvements.