from crewai import Task
from agents import pro_gambler, cricket_researcher, cricket_analyst

#TODO: We have to create the necessary tasks for the project

# Research Tasks
gather_match_data = Task(
    description=(
        "Gather data on the future cricket game, {cricket_match}"
    ),
    expected_output=(
        "Detailed information about the cricket match, including teams, players, "
        "venue, and match format of the both teams."
    ),
    agent=cricket_researcher
)

gather_historical_data = Task(
    description=(
        "Gather historical data on the cricket matches played by each team"
    ),
    expected_output=(
        "Detailed information about the each team's past performance, including the"
        "highlights of the match, outcome, and any notable information"
    ),
    context=[gather_match_data],
    agent=cricket_researcher
)

gather_player_data = Task(
    description=(
        "Gather data on the players of each team, including their past performance"
    ),
    expected_output=(
        "Detailed information about the players, including their statistics, "
        "performance history, and any notable achievements"
    ),
    context=[gather_match_data],
    agent=cricket_researcher
)

# Analysis Tasks
analyse_match_data = Task(
    description=(
        "AAnalyze the data gathered on the cricket match, including the team."
        "performance, player statistics, and historical data"
    ),
    expected_output=(
        "A comprehensive analysis of the match data, including insights into "
        "team strengths and weaknesses, player performance, and any trends or "
        "patterns observed in the data"
    ),
    context=[gather_match_data, gather_historical_data, gather_player_data],
    agent=cricket_analyst,
    output_file="match_analysis.md"
)

statistical_analysis = Task(
    description=(
        "Perform a statistical analysis of the match data, including "
        "cCalcCalculating averages, percentages, and other relevant statistics"
    ),
    expected_output=(
        "A detailed statistical analysis of the match data, including "
        "calculations of averages, percentages, and other relevant statistics"
    ),
    context=[analyse_match_data],
    agent=cricket_analyst,
    output_file="statistical_analysis.md"
)

# Gambling Tasks

next_gambles = Task(
    description=(
        "Based on the analysis of the match data, provide recommendations for "
        "the next gambles to place a budget of {budget} on the cricket match for"
        "a risk threshold of {risk_threshold} using {betting_strategy} betting strategy"
    ),
    expected_output=(
        "A list of recommended gambles to place, including the odds for each gamble, "
        "the potential payout, and any other relevant information, risk analysis, "
        "and the reasoning behind each recommendation"
    ),
    context=[statistical_analysis],
    agent=pro_gambler,
    output_file="next_gambles.md"
)

tasks: list[Task] = [
    gather_match_data,
    gather_historical_data,
    gather_player_data,
    analyse_match_data,
    statistical_analysis,
    next_gambles
]

__all__ = ["tasks"]