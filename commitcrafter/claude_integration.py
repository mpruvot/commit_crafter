import os
from anthropic import Anthropic


def get_claude_client() -> Anthropic:
    """Get a Claude client with the API key from the environment variables."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("Anthropic API key not found in environment variables")
    return Anthropic(api_key=api_key)


def generate_commit_names_using_chat(diff):
    """Generate commit names using the chat endpoint of the Claude API."""
    prompts_path = os.path.join(os.path.dirname(__file__), "prompt.txt")

    client = get_claude_client()

    with open(prompts_path, "r") as file:
        prompt = file.read()

    response = client.messages.create(
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
    commit_names = [commit_text.strip()]

    return commit_names
