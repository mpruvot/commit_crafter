from typing import TypeVar, Type
from openai import OpenAI
from anthropic import Anthropic
import os

T = TypeVar("T", OpenAI, Anthropic)


def get_client(client_type: Type[T], env_var: str) -> T:
    """
    Generic factory function for AI clients.
    """
    api_key = os.getenv(env_var)
    if not api_key:
        raise ValueError(f"{env_var} not found in environment variables")
    return client_type(api_key=api_key)
