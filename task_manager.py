from task import Task
from colors import RED, GREEN, YELLOW, RESET

class TaskManager:
    def __init__(self):
        self.next_id = 0
        self.tasks = []

    def get_next_id(self):
        current_id = self.next_id
        self.next_id += 1
        return current_id

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def add_task(self, name):
        if not name:
            print(f"{RED}Please provide a task name.{RESET}")
            return None
        new_id = self.get_next_id()
        task = Task(id=new_id, name=name)
        self.tasks.append(task)
        print(f"{GREEN}Task added successfully (ID: {task.id}){RESET}")
        return task

    def delete_task(self, task_id_str):
        try:
            task_id = int(task_id_str)
        except ValueError:
            print(f"{RED}'{task_id_str}' is not a valid task number.{RESET}")
            return None

        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f"{GREEN}Task removed successfully (ID: {task.id}){RESET}")
            return task

        print(f"{RED}Task not found (ID: '{task_id}') {RESET}")
        return None

    def update_task(self, args):
        parts = args.split(maxsplit=1)
        if len(parts) < 2:
            print(f"{RED}Please provide both a task ID and a new name.{RESET}")
            return None

        task_id_str, new_name = parts
        try:
            task_id = int(task_id_str)
        except ValueError:
            print(f"{RED}'{task_id_str}' is not a valid task number.{RESET}")
            return None

        task = self.get_task_by_id(task_id)
        if task:
            task.update_name(new_name)
            print(f"{GREEN}Task updated successfully (ID: {task.id}){RESET}")
            return task

        print(f"{RED}Task not found (ID: '{task_id}') {RESET}")
        return None

    def mark_task(self, args):
        parts = args.split(maxsplit=1)
        if len(parts) < 2:
            print(f"{RED}Please provide both a task ID and a new status.{RESET}")
            return None

        task_id_str, status = parts
        try:
            task_id = int(task_id_str)
        except ValueError:
            print(f"{RED}'{task_id_str}' is not a valid task number.{RESET}")
            return None

        task = self.get_task_by_id(task_id)
        if task:
            try:
                task.update_status(status)
                print(f"{GREEN}Task status updated to '{status}' (ID: {task.id}){RESET}")
                return task
            except ValueError as e:
                print(f"{RED}{e}{RESET}")
                return None

        print(f"{RED}Task not found (ID: '{task_id}') {RESET}")
        return None

    def list_tasks(self, status=None):
        if status == "":
            status = None
        filtered_tasks = [
            task for task in self.tasks
            if status is None or task.status == status.lower()
        ]

        if not filtered_tasks:
            print(f"{RED}No tasks found.{RESET}")
            return

        for task in filtered_tasks:
            color = (
                GREEN if task.status == "done"
                else YELLOW if task.status == "in-progress"
                else RESET
            )
            print(f"[{task.id}] {task.name} - {color}{task.status}{RESET}")
        if status == None:
            print(f"{YELLOW}Tip: You can type 'list done', 'list todo', or 'list in-progress' to filter your tasks.{RESET}")
