import json
import os
from task import Task
from task_manager import TaskManager

def save_tasks(task_manager, filename="tasks.json"):
    """
    Save the current task manager state to a JSON file.
    This includes the next available ID and the list of tasks.
    """
    data = {
        "next_id": task_manager.next_id,
        "tasks": [
            {"id": t.id, "name": t.name, "status": t.status}
            for t in task_manager.tasks
        ]
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_tasks(filename="tasks.json"):
    """
    Load task manager data from a JSON file.
    If the file doesn't exist, return a fresh TaskManager.
    """
    if not os.path.exists(filename):
        return TaskManager()

    with open(filename, "r") as f:
        data = json.load(f)

    manager = TaskManager()
    manager.next_id = data.get("next_id", 0)

    for item in data.get("tasks", []):
        task = Task(id=item["id"], name=item["name"], status=item["status"])
        manager.tasks.append(task)

    return manager
