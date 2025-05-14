from agno.playground import Playground, serve_playground_app
from agentic_task_app.agents.task_extractor_agent import TaskExtractorAgent

task_extractor_agent = TaskExtractorAgent()

app = Playground(agents=[task_extractor_agent.agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("main:app", reload=True)