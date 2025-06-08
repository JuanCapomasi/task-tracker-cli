from colors import RED, RESET

class Task:
    def __init__(self, id, name, status="todo"):
        self.id = id
        self.name = name
        self.status = status.lower()

    def update_name(self, new_name):
        self.name = new_name.strip()

    def update_status(self, new_status):
        valid_statuses = ["todo", "in-progress", "done"]
        if new_status.lower() not in valid_statuses:
            raise ValueError(f"{RED}Invalid status: '{new_status}'. Must be one of {valid_statuses}{RESET}")
        self.status = new_status.lower()

    def __str__(self):
        return f"Task(id={self.id}, name={self.name}, status={self.status})"