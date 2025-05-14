from crewai import LLM

llm = LLM(
    model="gpt-4o-mini",
    temperature=0.7
)

__all__ = ["llm"]