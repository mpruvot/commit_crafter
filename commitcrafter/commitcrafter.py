# commitcrafter.py
import os
from git import Repo
from git.exc import InvalidGitRepositoryError

from commitcrafter.exceptions import EmptyDiffError
from commitcrafter.gpt_integration import generate_commit_names_using_chat as gptapi
from commitcrafter.claude_integration import (
    generate_commit_names_using_chat as claudeapi,
)


class CommitCrafter:
    def __init__(self, path: str = os.getcwd(), compare_to: str = None):
        self.path = path
        self.compare_to = compare_to

    def generate(self, client: str = "gpt") -> list[str] | str:
        """
        Generate commit names based on the latest git diff. Returns a list of commit names.
        Args:
            client (str): The AI client to use ("gpt" or "claude")
        Raises:
            ValueError: If the API key is not found in the environment variables.
            EmptyDiffError: If no changes are found in the latest commit.
        """
        diff = self._get_latest_diff()

        if not diff:
            raise EmptyDiffError

        try:
            match client:
                case "gpt":
                    return gptapi(diff)
                case "claude":
                    return claudeapi(diff)
                case _:
                    raise ValueError(f"Unknown client: {client}")
        except ValueError:
            raise

    def _get_latest_diff(self) -> str:
        """
        Get the latest diff from the git repository at the given path.
        Args:
        repo_path (str): The path to the git repository.
        compare_to (str): The commit to compare the latest commit to.
        """
        try:
            repo = Repo(self.path, search_parent_directories=True)
        except InvalidGitRepositoryError as e:
            raise e
        hcommit = repo.head.commit
        diff = hcommit.diff(self.compare_to, create_patch=True)
        diff_text = "".join([d.diff.decode() if d.diff else "" for d in diff])
        return diff_text
