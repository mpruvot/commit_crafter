import os

from openai import OpenAI


def get_openai_client() -> OpenAI:
    """Get an OpenAI client with the API key from the environment variables."""
    api_key = os.getenv("COMMITCRAFT_OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OpenAI API key not set.-> export COMMITCRAFT_OPENAI_API_KEY=<your_api_key>"
            " or add it to you shell profile."
        )
    return OpenAI(api_key=api_key)


def generate_commit_names_using_chat(diff):
    """Generate commit names using the chat endpoint of the OpenAI API."""
    prompts_path = os.path.join(os.path.dirname(__file__), "prompt.txt")

    client = get_openai_client()

    with open(prompts_path, "r") as file:
        prompt = file.read()

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": diff},
    ]

    response = client.chat.completions.create(
        model=os.environ.get("GPT_MODEL", "gpt-3.5-turbo"),
        messages=messages,
        max_tokens=150,
    )

    commit_names = [response.choices[0].message.content.strip()]
    return commit_names
