from anthropic import Anthropic
from commitcrafter.ai_client_factory import get_client
from commitcrafter.ai_client_repository import AIClientRepository


class ClaudeClient(AIClientRepository[Anthropic]):
    """Claude implementation of AI client repository."""

    def __init__(self):
        client = get_client(Anthropic, "ANTHROPIC_API_KEY")
        super().__init__(client)

    def generate_commit_messages(self, diff: str, prompt: str) -> list[str]:
        """Generate commit messages using the Claude API."""
        response = self.client.messages.create(
            system=prompt,
            max_tokens=200,
            messages=[
                {
                    "role": "user",
                    "content": diff,
                }
            ],
            model="claude-3-5-sonnet-20241022",
        )

        commit_text = (
            response.content[0].text
            if isinstance(response.content, list)
            else response.content.text
        )
        return [commit_text.strip()]
