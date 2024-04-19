import os

from git import Repo
from git.exc import InvalidGitRepositoryError

from commitcrafter.exceptions import EmptyDiffError
from commitcrafter.gpt_integration import generate_commit_names_using_chat


class CommitCrafter:
    def __init__(self, path: str = os.getcwd(), compare_to: str = None):
        self.path = path
        self.compare_to = compare_to

    def _get_latest_diff(self) -> str:
        """
        Get the latest diff from the git repository at the given path.
        Args:
        repo_path (str): The path to the git repository.
        compare_to (str): The commit to compare the latest commit to.
        """
        try:
            repo = Repo(self.path, search_parent_directories=True)
        except InvalidGitRepositoryError:
            raise ValueError(f" :x: No git repository found at {self.path} :x:")
        hcommit = repo.head.commit
        diff = hcommit.diff(self.compare_to, create_patch=True)
        diff_text = "".join([d.diff.decode() if d.diff else "" for d in diff])
        return diff_text

    def generate(self) -> list[str] | str:
        """
        Generate commit names based on the latest git diff. Returns a list of commit names.
        Raises:
            ValueError: If the OpenAI API key is not found in the environment variables.
            EmptyDiffError: If no changes are found in the latest commit.
        """
        try:
            diff = self._get_latest_diff()
        except ValueError as e:
            return str(e)

        if diff:
            try:
                commit_names = generate_commit_names_using_chat(diff)
                return commit_names
            except ValueError as e:
                raise e
        else:
            raise EmptyDiffError
