from crewai import Crew, Process
from dotenv import load_dotenv

load_dotenv()

from agents import agents
from tasks import tasks

# Initialize the Crew
crew = Crew(
    agents=agents,
    tasks=tasks,
    process= Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the Cricket Gambler.")
    parser.add_argument(
        "--cricket_match",
        type=str,
        required=True,
        help="The name of the cricket match to bet on (e.g., 'India vs Australia on 2023-10-01').",
    )
    parser.add_argument(
        "--budget",
        type=str,
        required=True,
        help="The budget for betting (e.g., '$100').",
    )
    parser.add_argument(
        "--betting_strategy",
        type=str,
        default="aggressive",
        help="The betting strategy to use (e.g., 'aggressive', 'conservative').",
    )
    parser.add_argument(
        "--risk_threshold",
        type=float,
        default=0.5,
        help="The risk threshold for betting (e.g., 0.5).",
    )

    args = parser.parse_args()

    input_data = {
        "cricket_match": args.cricket_match,
        "budget": args.budget,
        "betting_strategy": args.betting_strategy,
        "risk_threshold": args.risk_threshold,
    }

    crew.kickoff(
        inputs=input_data,
    )