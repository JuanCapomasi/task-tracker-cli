# task-tracker-cli
CLI test #1 Task Tracker
Clone the repo:

git clone https://github.com/your-username/tasktrack.git
cd tasktrack

Run it:
python main.py


Usage

add <task>                  → Add a new task
delete <task number>        → Remove a task
update <task number> <new title> → Rename a task
mark <task number> <status> → Change task status (todo, done, in-progress)
list                        → Show all tasks
list done|todo|in-progress  → Filtered list
help                        → Show help
exit / quit                 → Exit the app

Aliases like rm, del, ls, q are supported.

Tests are written using the unittest module. Run all tests with:

python -m unittest discover -s tests

https://roadmap.sh/projects/task-tracker