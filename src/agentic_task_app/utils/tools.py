from agno.tools import tool
import uuid
from datetime import datetime

@tool(show_result=True)
def generate_task_id() -> str:
    """
    Generate a unique task identifier.

    Returns:
        str: A unique task identifier.
    """
    return str(uuid.uuid4())

@tool(show_result=True)
def get_current_timestamp() -> str:
    """
    Get the current timestamp in ISO 8601 format.

    Returns:
        str: Current timestamp in ISO 8601 format.
    """
    return datetime.now().isoformat()