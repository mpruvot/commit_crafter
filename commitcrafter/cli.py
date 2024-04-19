import typer
from rich import print

from commitcrafter.commitcrafter import CommitCrafter
from commitcrafter.exceptions import EmptyDiffError

app = typer.Typer()


@app.command()
def generate():
    """Generate commit names based on the latest git diff."""
    try:
        commit_names = CommitCrafter().generate()
        for name in commit_names:
            print(name)
    except ValueError as e:
        print(
            f"[bold red]{e}[/bold red] : Please set the COMMITCRAFT_OPENAI_API_KEY environment variable.\n\n"
            f"=> export COMMITCRAFT_OPENAI_API_KEY='your-api-key' <="
        )
    except EmptyDiffError as e:
        print(e)


if __name__ == "__main__":
    app()
