import os
from git import Repo
from git.exc import InvalidGitRepositoryError
from .exceptions import EmptyDiffError
from .commit_generator import CommitGenerator
from .models import CommitMessage, AIModel


class CommitCrafter:
    """Main class for generating commit messages from git diffs."""

    def __init__(
        self,
        path: str = os.getcwd(),
        ai_model: AIModel = AIModel.CLAUDE,
    ):
        self.path = path
        self._generator = self._init_generator(ai_model)

    @staticmethod
    def _init_generator(model_name: AIModel) -> CommitGenerator:
        return CommitGenerator(model_name)

    def generate(
        self,
    ) -> list[CommitMessage]:
        """
        Generate commit messages based on the latest git diff.
        Returns:
            List of formatted commit messages

        Raises:
            EmptyDiffError: If no changes are found
            InvalidGitRepositoryError: If no git repository is found
            ValueError: If model generation fails
        """

        diff = self._get_latest_diff()
        self._check_diff_is_not_empty(diff)
        try:
            return self._generator.generate_commits_sync(diff)
        except Exception as e:
            raise ValueError(f"Failed to generate commit messages: {str(e)}") from e

    @staticmethod
    def _check_diff_is_not_empty(diff) -> None:
        if not diff:
            raise EmptyDiffError("No changes found in the working directory")
        return None

    def _get_latest_diff(self) -> str:
        """
        Get the latest diff from the git repository.

        Returns:
            The git diff as text

        Raises:
            InvalidGitRepositoryError: If no git repository is found
        """
        try:
            repo = Repo(self.path, search_parent_directories=True)
        except InvalidGitRepositoryError as e:
            raise InvalidGitRepositoryError(
                f"No git repository found at {self.path}"
            ) from e

        hcommit = repo.head.commit
        diff = hcommit.diff(None, create_patch=True)
        return "".join(d.diff.decode() if d.diff else "" for d in diff)
