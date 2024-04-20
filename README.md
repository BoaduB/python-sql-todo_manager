git clone https://your-repository-url.git
cd todo_list_manager
python --version
# Make sure the output is Python 3.x
python --version

To add a new task, use the -a or --add option followed by the task description in quotes:
python todo_manager.py -a "Finish the monthly report"

To remove a task, you need its ID. Use the -r or --remove option followed by the task ID:
python todo_manager.py -r 2

To mark a task as completed, use the -m or --mark-complete option followed by the task ID:
python todo_manager.py -m 3

To list all tasks in your todo list, use the -l or --list option:
python todo_manager.py -l

For more information or to view the help documentation, use the -h or --help option:
python todo_manager.py -h