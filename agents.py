from crewai import Agent
from crewai_tools import SerperDevTool, CodeInterpreterTool
from llm import llm


cricket_researcher = Agent(
    role="Expert Cricket Researcher",
    goal=(
        "Gather information for the {cricket_match} match, including player stats, team performance Both teams and weather conditions."
        "Look for any recent news or updates that might affect the match, Previous match results, and any other relevant information."
        "Provide a summary of the findings and any insights that could be useful for the match analysis. including the source citations."
    ),
    backstory="An expert cricket researcher with a deep understanding of the cricket and its statistics.",
    llm=llm,
    tools=[SerperDevTool()],
)

cricket_analyst = Agent(
    role="Expert Cricket Analyst",
    goal=(
        "Analyze the gathered information and provide insights on the match, including player performance, team strategies, and potential outcomes."
        "Look for any patterns or trends that could influence the match result."
    ),
    backstory="An expert cricket analyst with a deep understanding of cricket strategies and statistics.",
    llm=llm,
    tools=[SerperDevTool(), CodeInterpreterTool(unsafe_mode=True)],
)

pro_gambler = Agent(
    role="Professional Cricket Gambler",
    goal=(
        "Based on the analysis, provide betting recommendations for the match, including odds and potential outcomes."
        "Consider the gathered information and analysis to make informed betting decisions."
    ),
    backstory="A professional gambler with a deep understanding of cricket betting strategies.",
    llm=llm
)

agents: list[Agent] = [cricket_researcher, cricket_analyst, pro_gambler]

__all__ = ["agents", "cricket_researcher", "cricket_analyst", "pro_gambler"]