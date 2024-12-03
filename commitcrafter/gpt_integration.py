from openai import OpenAI
from commitcrafter.ai_client_repository import AIClientRepository
from commitcrafter.ai_client_factory import get_client
import os


class GPTClient(AIClientRepository[OpenAI]):
    """OpenAI implementation of AI client repository."""

    def __init__(self):
        client = get_client(OpenAI, "COMMITCRAFT_OPENAI_API_KEY")
        super().__init__(client)

    def generate_commit_messages(self, diff: str, prompt: str) -> list[str]:
        """Generate commit messages using the OpenAI API."""
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": diff},
        ]

        response = self.client.chat.completions.create(
            model=os.environ.get("GPT_MODEL", "gpt-3.5-turbo"),
            messages=messages,
            max_tokens=150,
        )

        return [response.choices[0].message.content.strip()]
