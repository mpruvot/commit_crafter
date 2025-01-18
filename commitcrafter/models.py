from enum import StrEnum

from pydantic import BaseModel, Field, field_validator


class CommitType(StrEnum):
    """Enumeration of valid commit types"""

    FEAT = "feat"
    FIX = "fix"
    DOCS = "docs"
    STYLE = "style"
    REFACTOR = "refactor"
    PERF = "perf"
    TEST = "test"
    CHORE = "chore"
    CI = "ci"


COMMIT_EMOJIS = {
    CommitType.FEAT: "✨ ",
    CommitType.FIX: "🐛 ",
    CommitType.DOCS: "📚 ",
    CommitType.STYLE: "💄 ",
    CommitType.REFACTOR: "♻️ ",
    CommitType.PERF: "⚡️ ",
    CommitType.TEST: "🧪 ",
    CommitType.CHORE: "🔧 ",
    CommitType.CI: "🎡 ",
}


class AIModel(StrEnum):
    CLAUDE = "anthropic:claude-3-5-sonnet-latest"
    GPT = "openai:gpt-3.5-turbo"
    GPT4 = "openai:gpt-4"
    GEMINI = "google-gla:gemini-1.5-flash"
    MISTRAL = "mistral:mistral-large-latest"
    OLLAMA = "ollama:llama3"

    @classmethod
    def get_provider(cls, model: str) -> str:
        return model.split(":")[0]


class Agent(StrEnum):
    CLAUDE = "claude"
    GPT = "gpt"
    GPT4 = "gpt4"
    GEMINI = "gemini"
    OLLAMA = "ollama"
    MISTRAL = "mistral"


AI_MODEL_MAP = {
    Agent.CLAUDE: AIModel.CLAUDE,
    Agent.GPT: AIModel.GPT,
    Agent.GPT4: AIModel.GPT4,
    Agent.GEMINI: AIModel.GEMINI,
    Agent.OLLAMA: AIModel.OLLAMA,
    Agent.MISTRAL: AIModel.MISTRAL,
}


class CommitMessage(BaseModel):
    """A structured commit message following conventional commits."""

    type: CommitType
    description: str = Field(..., max_length=50)

    @field_validator("description")
    def validate_description(cls, v: str) -> str:
        if v[0].isupper():
            raise ValueError("description should not start with a capital letter")
        if v.endswith("."):
            raise ValueError("description should not end with a period")
        if v.endswith("ed") or v.endswith("ing"):
            raise ValueError("description should use imperative mood")
        return v

    def __str__(self) -> str:
        return f"{COMMIT_EMOJIS[self.type]} {self.type.value}: {self.description}"
