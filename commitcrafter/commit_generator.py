from typing import List
from pydantic_ai import Agent
import os

from commitcrafter.models import CommitMessage, CommitType, AIModel


class CommitGenerator:
    """Generator for conventional commit messages using AI."""

    def __init__(self, ai_model: AIModel = AIModel.CLAUDE):
        self._validate_api_key(ai_model)
        system_prompt = self._get_prompt()
        self.agent = Agent(
            ai_model, result_type=List[CommitMessage], system_prompt=system_prompt
        )

    @staticmethod
    def _get_prompt() -> str:
        """Get the prompt from the prompt.txt file."""
        prompts_path = os.path.join(os.path.dirname(__file__), "prompt.txt")
        try:
            with open(prompts_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Prompt file not found at {prompts_path}. "
                "Make sure prompt.txt is included in your package."
            )
        except Exception as e:
            raise RuntimeError(f"Error reading prompt file: {str(e)}")

    @staticmethod
    def _validate_api_key(model: AIModel) -> None:
        """Validate that the required API key is set."""
        provider = AIModel.get_provider(model)
        match provider:
            case "openai" | "anthropic" | "ollama" | "mistral":
                env_var = f"{provider.upper()}_API_KEY".replace("-", "_")
                if not os.getenv(env_var):
                    raise ValueError(
                        f"{provider.title()} API key not found. Please set the {env_var} environment variable.\n"
                        f"export {env_var}='your-api-key'"
                    )
            case "google-gla":
                env_var = f"GEMINI_API_KEY"
                if not os.getenv(env_var):
                    raise ValueError(
                        f"{provider.title()} API key not found. Please set the {env_var} environment variable.\n"
                        f"export {env_var}='your-api-key'"
                    )

            case _:
                raise ValueError(f"Unknown model: {provider}")

    def generate_commits_sync(self, diff: str) -> List[CommitMessage]:
        """Generate commit messages synchronously."""
        result = self.agent.run_sync(diff)
        commits = result.data
        if len(commits) != 5:
            raise ValueError(f"Expected exactly 5 commits, got {len(commits)}")
        return commits
