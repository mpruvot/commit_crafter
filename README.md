# CommitCrafter

CommitCrafter is a Python command-line application that leverages the power of OpenAI's GPT models to generate descriptive and concise names for your Git commits. It analyzes code differences (diffs) and automates the naming process to streamline your workflow.

## Table of Contents

- [CommitCrafter](#commitcrafter)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
  - [Setup](#setup)
    - [Install the project dependencies:](#install-the-project-dependencies)
  - [Usage](#usage)
    - [Configuration](#configuration)
    - [Generating Commit Names](#generating-commit-names)

## Project Overview

CommitCrafter simplifies the task of creating meaningful commit messages by interpreting code changes and providing suggestions that reflect the nature and significance of those changes. Whether it's a bug fix, performance improvement, new feature, or general update, CommitCrafter crafts a suitable commit message to save you time and effort.

## Installation

### Prerequisites

Before installing CommitCrafter, ensure you have Python installed on your system. CommitCrafter is compatible with Python 3.6 and above.

## Setup

Clone the repository to your local machine and navigate to the project directory:

```bash
git clone https://github.com/mpruvot/CommitCrafter.git
cd CommitCrafter
````
### Install the project dependencies:

```
pip install -e .
````

## Usage

### Configuration
To configure CommitCrafter, you'll need to set up your environment with your OpenAI API key.

- Run the setup command:
```
commitcraft setup
```
- Follow the prompts to enter your OpenAI API key and select the desired GPT model.

- The setup will create a .env file that stores your API key and model selection securely.

### Generating Commit Names
With CommitCrafter installed and configured, you can now generate commit names by running:

```
commitcraft generate
```
This will fetch the latest diff from your Git repository and provide you with commit name suggestions.

