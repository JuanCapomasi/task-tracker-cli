from storage import save_tasks, load_tasks
from colors import RED, GREEN, YELLOW, CYAN, RESET

def display_help():
    commands = [
        ("add <task>", "Add a new task"),
        ("delete <task number>", "Remove a task by its number"),
        ("update <task number> <new title>", "Change the title of a task"),
        ("mark <task number> done", "Mark a task as finished"),
        ("mark <task number> todo", "Mark a task as to-do"),
        ("mark <task number> in-progress", "Mark a task as in progress"),
        ("list", "Show all tasks"),
        ("list done", "Show only completed tasks"),
        ("list todo", "Show only to-do tasks"),
        ("list in-progress", "Show tasks in progress"),
        ("help", "Show this help message"),
        ("exit or quit", "Close the app"),
    ]

    max_length = max(len(command) for command, _ in commands)

    print(f"\n{YELLOW}Here’s what you can do:\n{RESET}")
    for command, description in commands:
        print(f"  {CYAN}{command.ljust(max_length)}{RESET}  → {description}")

def main():
    manager = load_tasks()

    aliases = {
        "rm": "delete",
        "del": "delete",
        "ls": "list",
        "quit": "exit",
        "q": "exit",
        "h": "help",
        "add": "add",
        "delete": "delete",
        "update": "update",
        "mark": "mark",
        "list": "list",
        "help": "help",
        "exit": "exit",
    }

    while True:
        print("\n ===== Tasktrack =====")
        clean_command = input("> ").strip()
        if not clean_command:
            continue

        parts = clean_command.split(maxsplit=1)
        action = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        action = aliases.get(action, action)

        if action == "add":
            manager.add_task(args)
            save_tasks(manager)
        elif action == "delete":
            manager.delete_task(args)
            save_tasks(manager)
        elif action == "update":
            manager.update_task(args)
            save_tasks(manager)
        elif action == "mark":
            manager.mark_task(args)
            save_tasks(manager)
        elif action == "list":
            manager.list_tasks(args.lower())
        elif action == "help":
            display_help()
        elif action == "exit":
            print(f"{GREEN}Thanks for using Tasktrack. See you next time!{RESET}")
            break
        else:
            print(f"{RED}Hmm, I didn’t understand '{action}'. Type 'help' to see what you can do.{RESET}")

if __name__ == "__main__":
    main()