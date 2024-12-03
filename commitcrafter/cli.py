import os
from typing import List
from enum import Enum
import typer
from git import InvalidGitRepositoryError
from rich import print
from rich.prompt import Prompt
from rich.console import Console

from commitcrafter.commitcrafter import CommitCrafter
from commitcrafter.exceptions import EmptyDiffError

app = typer.Typer()
console = Console()


class AIClient(str, Enum):
    GPT = "gpt"
    CLAUDE = "claude"


class CommitType(str, Enum):
    FEAT = "feat"
    FIX = "fix"
    DOCS = "docs"
    STYLE = "style"
    REFACTOR = "refactor"
    PERF = "perf"
    TEST = "test"
    CHORE = "chore"
    CI = "ci"


def parse_commits(commit_text: str) -> List[str]:
    """
    Parse commits from the raw text response.

    Args:
        commit_text: Raw text containing commit messages

    Returns:
        List of parsed commit messages
    """
    lines = commit_text.strip().split("\n")
    commits = []

    for line in lines:
        cleaned = line.lstrip("0123456789. ")
        if cleaned and any(f"{type.value}:" in cleaned for type in CommitType):
            commits.append(cleaned.strip())

    return commits


def select_commit(commits: list[str]) -> str | None:
    """
    Allow user to select a commit message interactively.

    Args:
        commits: List of commit messages to choose from

    Returns:
        Selected commit message or None if no commits available
    """
    if not commits:
        console.print("[yellow]No valid commit messages found[/yellow]")
        return None

    for idx, commit in enumerate(commits, 1):
        print(f"{idx}. {commit}")

    choices = [str(i) for i in range(1, len(commits) + 1)]
    choice = Prompt.ask(
        "\nSelect a commit message",
        choices=choices,
        default="1",
    )

    return commits[int(choice) - 1]


def copy_to_clipboard(message: str) -> None:
    """Try to copy message to clipboard and notify user."""
    try:
        import pyperclip

        pyperclip.copy(message)
        console.print("\n✨ [green]Commit message copied to clipboard![/green]")
    except ImportError:
        console.print(f"\n✨ Selected commit message: [blue]{message}[/blue]")


@app.command()
def generate(
    client: AIClient = typer.Option(
        AIClient.GPT,
        "--client",
        "-c",
        help="Choose AI Client to generate your commit message",
        case_sensitive=False,
    ),
) -> None:
    """Generate commit names based on the latest git diff."""
    try:
        commit_crafter = CommitCrafter()
        raw_commits = commit_crafter.generate(client=client.value)

        # Handle different return types
        commit_text = raw_commits[0] if isinstance(raw_commits, list) else raw_commits
        commit_messages = parse_commits(commit_text)

        if selected_commit := select_commit(commit_messages):
            copy_to_clipboard(selected_commit)

    except ValueError as e:
        if client == AIClient.GPT:
            console.print(
                f"[bold red]{e}[/bold red]: Please set the COMMITCRAFT_OPENAI_API_KEY environment variable.\n\n"
                f"export COMMITCRAFT_OPENAI_API_KEY='your-api-key'"
            )
        else:
            console.print(
                f"[bold red]Anthropic API key not found[/bold red]: Please set the ANTHROPIC_API_KEY environment variable.\n\n"
                f"export ANTHROPIC_API_KEY='your-api-key'"
            )
    except EmptyDiffError:
        console.print(
            "[bold yellow]No changes found in the latest commit[/bold yellow]"
        )
    except InvalidGitRepositoryError:
        console.print(
            f":neutral_face: [bold red]No git repository found at {os.getcwd()}[/bold red] :neutral_face:"
        )


if __name__ == "__main__":
    app()
