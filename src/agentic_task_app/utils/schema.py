from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    """Task model for the agentic task app."""

    name: str = Field(..., description="Name of the task")
    description: str = Field(..., description="Description of the task")
    status: str = Field(
        ..., description="Status of the task (e.g., 'pending', 'completed')"
    )
