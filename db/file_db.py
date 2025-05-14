import json
import os
from db.base import BaseDB

DB_FILE = "tasks.json"

class FileDB(BaseDB):
    def __init__(self):
        if not os.path.exists(DB_FILE):
            with open(DB_FILE, "w") as f:
                json.dump([], f)

    def save_task(self, task: dict):
        with open(DB_FILE, "r+") as f:
            tasks = json.load(f)
            tasks.append(task)
            f.seek(0)
            json.dump(tasks, f, indent=2)

    def get_tasks(self, user_id: str):
        with open(DB_FILE) as f:
            tasks = json.load(f)
            return [t for t in tasks if t["user_id"] == user_id]
