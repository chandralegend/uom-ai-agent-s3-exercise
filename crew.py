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
    pass