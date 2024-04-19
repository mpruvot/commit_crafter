# CommitCrafter

**CommitCrafter** is an AI-powered tool designed to enhance Git workflows by generating descriptive commit messages
based on changes made within the repository. Utilizing the OpenAI API, it provides a seamless way to create meaningful
commit names that accurately reflect the content of your updates.

## Features

- **AI-Generated Commit Messages**: Automatically generates descriptive commit messages using the power of GPT models.
- **Easy Integration**: Directly integrates with your Git repositories to analyze recent diffs.
- **Customization Options**: Modify the AI prompts to better match your project’s context and coding conventions.

## Installation

CommitCrafter requires Python 3.12 or newer. Install CommitCrafter globally with pipx to ensure it is available in any
of your projects:

```bash
pipx install commitcrafter
```

## Usage

To use CommitCrafter, navigate to your project directory and execute:

```bash
commitcraft
```

#### Make sure to export your OpenAI API key in your environment variables:

```bash
export COMMITCRAFT_OPENAI_API_KEY='your-api-key'
```

## Dependencies

- Python (>=3.12)
- GitPython
- Typer for command-line interfaces
- Rich for formatting terminal outputs
