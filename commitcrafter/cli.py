import typer

from .git_tools import get_latest_diff
from .gpt_integration import generate_commit_names_using_chat

app = typer.Typer()


@app.command()
def generate():
    """Generate commit names based on the latest git diff."""
    diff = get_latest_diff()
    if diff:
        commit_names = generate_commit_names_using_chat(diff)
        for name in commit_names:
            typer.echo(name)
    else:
        typer.echo("No diff found or diff is empty.")


if __name__ == "__main__":
    app()
