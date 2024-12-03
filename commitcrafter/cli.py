import os
from typing import List

import typer
from git import InvalidGitRepositoryError
from rich import print
from rich.prompt import Prompt
from enum import Enum

from commitcrafter.commitcrafter import CommitCrafter
from commitcrafter.exceptions import EmptyDiffError


app = typer.Typer()


class AIClient(str, Enum):
    GPT = "gpt"
    CLAUDE = "claude"


def parse_commits(commit_text: str) -> List[str]:
    """Parse commits from the raw text response."""
    lines = commit_text.strip().split("\n")
    commits = []

    for line in lines:
        cleaned = line.lstrip("0123456789. ")
        if cleaned and any(
            type in cleaned
            for type in [
                "feat:",
                "fix:",
                "docs:",
                "style:",
                "refactor:",
                "perf:",
                "test:",
                "chore:",
                "ci:",
            ]
        ):
            commits.append(cleaned.strip())

    return commits


def select_commit(commits: List[str]) -> str:
    """Allow user to select a commit message using arrow keys."""
    for idx, commit in enumerate(commits, 1):
        print(f"{idx}. {commit}")

    choice = Prompt.ask(
        "\nSelect a commit message [1-5]",
        choices=[str(i) for i in range(1, len(commits) + 1)],
        default="1",
    )

    return commits[int(choice) - 1]


@app.command()
def generate(
    client: AIClient = typer.Option(
        AIClient.GPT,
        "--client",
        "-c",
        help="Choose AI Client To generate your commit message.",
        case_sensitive=False,
    ),
):
    """Generate commit names based on the latest git diff."""
    try:
        commit_crafter = CommitCrafter()
        raw_commits = commit_crafter.generate(client=client.value)

        if isinstance(raw_commits, list):
            raw_commits = raw_commits[0]

        commit_names = parse_commits(raw_commits)

        if commit_names:
            selected = select_commit(commit_names)
            try:
                import pyperclip

                pyperclip.copy(selected)
                print("\n✨ Commit message copied to clipboard!")
            except ImportError:
                print(f"\n✨ Selected commit message: {selected}")

    except ValueError as e:
        if client == AIClient.GPT:
            print(
                f"[bold red]{e}[/bold red] : Please set the COMMITCRAFT_OPENAI_API_KEY environment variable.\n\n"
                f"export COMMITCRAFT_OPENAI_API_KEY='your-api-key'"
            )
        else:
            print(
                f"[bold red]Anthropic API key not found[/bold red] : Please set the ANTHROPIC_API_KEY environment variable.\n\n"
                f"export ANTHROPIC_API_KEY='your-api-key'"
            )
    except EmptyDiffError:
        print("[bold]No changes found in the latest commit[/bold]")
    except InvalidGitRepositoryError:
        print(
            f":neutral_face: [bold]No git repository found at {os.getcwd()}[bold] :neutral_face:"
        )


if __name__ == "__main__":
    app()
