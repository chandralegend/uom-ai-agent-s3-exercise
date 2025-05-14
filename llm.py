from crewai import LLM

llm = LLM(
    model="mistral/mistral-large-latest",
    temperature=0.7
)

__all__ = ["llm"]