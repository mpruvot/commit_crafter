import os

import typer

from .git_tools import get_latest_diff
from .gpt_integration import generate_commit_names_using_chat

app = typer.Typer()


@app.command()
def generate():
    """Generate commit names based on the latest git diff."""
    diff = get_latest_diff(os.getcwd())
    if diff:
        try:
            commit_names = generate_commit_names_using_chat(diff)
            for name in commit_names:
                typer.echo(name)
        except ValueError as e:
            typer.echo(str(e))
    else:
        typer.echo("No diff found or diff is empty.")


if __name__ == "__main__":
    app()
