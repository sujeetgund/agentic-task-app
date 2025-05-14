from abc import ABC, abstractmethod

class BaseDB(ABC):
    @abstractmethod
    def save_task(self, task: dict): pass

    @abstractmethod
    def get_tasks(self, user_id: str): pass
