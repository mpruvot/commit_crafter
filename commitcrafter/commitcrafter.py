import os
from typing import Literal
from git import Repo
from git.exc import InvalidGitRepositoryError
from commitcrafter.exceptions import EmptyDiffError
from commitcrafter.ai_client_repository import AIClientRepository
from commitcrafter.gpt_integration import GPTClient
from commitcrafter.claude_integration import ClaudeClient

ClientType = Literal["gpt", "claude"]


def get_prompt() -> str:
    """Get the prompt from the prompt.txt file."""
    prompts_path = os.path.join(os.path.dirname(__file__), "prompt.txt")
    with open(prompts_path, "r") as file:
        return file.read()


class CommitCrafter:
    def __init__(
        self,
        path: str = os.getcwd(),
        compare_to: str = None,
        prompt: str = get_prompt(),
    ):
        self.path = path
        self.compare_to = compare_to
        self.prompt = prompt
        self._clients: dict[ClientType, AIClientRepository] = {}

    def _get_client(self, client_type: ClientType) -> AIClientRepository:
        """Get or create client on demand."""
        if client_type not in self._clients:
            if client_type == "gpt":
                self._clients[client_type] = GPTClient()
            elif client_type == "claude":
                self._clients[client_type] = ClaudeClient()
        return self._clients[client_type]

    def generate(self, client: ClientType = "gpt") -> list[str]:
        """
        Generate commit names based on the latest git diff.
        Args:
            client: The AI client to use ("gpt" or "claude")
        Returns:
            List of generated commit messages
        Raises:
            ValueError: If the API key is not found or client is invalid
            EmptyDiffError: If no changes are found in the latest commit
        """
        if client not in ["gpt", "claude"]:
            raise ValueError(f"Unknown client: {client}")

        diff = self._get_latest_diff()
        if not diff:
            raise EmptyDiffError

        try:
            return self._get_client(client).generate_commit_messages(
                diff=diff, prompt=self.prompt
            )
        except ValueError as e:
            raise ValueError(f"Error with {client} client: {str(e)}") from e

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
        diff = hcommit.diff(self.compare_to, create_patch=True)
        return "".join(d.diff.decode() if d.diff else "" for d in diff)
