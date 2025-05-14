from agno.agent import Agent, RunResponse
from agno.models.groq import Groq

from agentic_task_app.config import TEXT_EXTRACTOR_AGENT_MODEL_ID
from agentic_task_app.utils.schema import TaskModel


class TaskExtractorAgent:
    """A class to extract tasks from a given text using an agent."""

    def __init__(self):
        self.agent = Agent(
            model=Groq(id=TEXT_EXTRACTOR_AGENT_MODEL_ID),
            name="Task Extractor Agent",
            description="An agent that extracts structured task details from natural language input and returns them in JSON format compliant with the TaskModel schema.",
            instructions="""
                Extract detailed information about a task from the user's input. Output a valid JSON object matching the TaskModel schema.

                Include the following fields:
                - name: A short title for the task.
                - description: A detailed description of what the task involves.
                - status: Default to "pending" unless specified otherwise.
            """,
            response_model=TaskModel,
        )

    def extract_tasks(self, text: str) -> RunResponse:
        """
        Extracts tasks from the given text using the agent.
        """
        if not text:
            raise ValueError("Input text cannot be empty.")
        try:
            return self.agent.run(text).content
        except Exception as e:
            print(f"Task extraction failed")
            raise RuntimeError(f"An error occurred while extracting tasks: {e}")


if __name__ == "__main__":
    text = "I have completed a meeting with John yesterday"
    task_extractor_agent = TaskExtractorAgent()
    response = task_extractor_agent.extract_tasks(text)
    print(response)
