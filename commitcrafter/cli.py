import os
import typer
from git import InvalidGitRepositoryError
from rich import print
from rich.prompt import Prompt
from rich.console import Console

from commitcrafter.commitcrafter import CommitCrafter
from commitcrafter.exceptions import EmptyDiffError
from commitcrafter.models import CommitMessage, Agent, AI_MODEL_MAP
import pyperclip

app = typer.Typer()
console = Console()


def select_commit(commits: list[CommitMessage]) -> CommitMessage | None:
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


def copy_to_clipboard(message: CommitMessage) -> None:
    """Try to copy message to clipboard and notify user."""
    try:
        pyperclip.copy(str(message))
        console.print("\n✨ [green]Commit message copied to clipboard![/green]")
    except ImportError:
        console.print(f"\n✨ Selected commit message: [blue]{message}[/blue]")


@app.command()
def generate(
    agent: Agent = typer.Option(
        Agent.CLAUDE,
        "--agent",
        "-a",
        help="Choose AI agent (claude/gpt/gemini/ollama/mistral)",
        case_sensitive=False,
    ),
) -> None:
    """Generate commit names based on the latest git diff."""
    try:
        commits = CommitCrafter(ai_model=AI_MODEL_MAP[agent]).generate()
        if selected_commit := select_commit(commits):
            copy_to_clipboard(selected_commit)

    except ValueError as e:
        console.print(f"[bold red]{e}[/bold red]")
    except EmptyDiffError:
        console.print(
            "[bold yellow]No changes found in the latest commit[/bold yellow]"
        )
    except InvalidGitRepositoryError:
        console.print(
            f":neutral_face: [bold red]No git repository found at {os.getcwd()}[/bold red] :neutral_face:"
        )
    except Exception as e:
        console.print(
            "[bold red]Oops, something went wrong & guess what? I've no idea what that is. So open an issue on GitHub and fix it.[/bold red]"
        )
        console.print(f"[bold red]{e}[/bold red]")


if __name__ == "__main__":
    app()
