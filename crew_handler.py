from crewai import Crew
from agent import tasks, agents


crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True,
    )


def execute_crew(topic, limit, style, tone):
    result = crew.kickoff(
        inputs={"topic": topic, "limit": limit, "style": style, "tone": tone}
    )
    return result
