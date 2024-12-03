from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar("T")


class AIClientRepository(Generic[T], ABC):
    """Abstract base class for AI client repositories."""

    def __init__(self, client: T):
        self.client = client

    @abstractmethod
    def generate_commit_messages(self, diff: str) -> List[str]:
        """Generate commit messages based on git diff."""
        pass
