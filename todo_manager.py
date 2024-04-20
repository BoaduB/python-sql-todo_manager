import sqlite3
import argparse
import sys

def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create a table if it doesn't already exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        task text NOT NULL,
        completed boolean NOT NULL DEFAULT 0
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def add_task(conn, task):
    """Add a new task to the tasks table."""
    sql = ''' INSERT INTO tasks(task)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (task,))
    conn.commit()
    return cur.lastrowid

def remove_task(conn, task_id):
    """Remove a task by task id."""
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (task_id,))
    conn.commit()

def mark_task_completed(conn, task_id):
    """Mark a task as completed."""
    sql = 'UPDATE tasks SET completed=1 WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (task_id,))
    conn.commit()

def list_tasks(conn):
    """List all tasks."""
    cur = conn.cursor()
    cur.execute("SELECT id, task, completed FROM tasks")
    rows = cur.fetchall()
    for row in rows:
        status = 'Completed' if row[2] else 'Pending'
        print(f"Task ID {row[0]}: {row[1]} - {status}")

def main():
    parser = argparse.ArgumentParser(description="Manage your todo list.")
    parser.add_argument("-a", "--add", type=str, help="Add a new task")
    parser.add_argument("-r", "--remove", type=int, help="Remove a task by task ID")
    parser.add_argument("-m", "--mark-complete", type=int, help="Mark a task as completed by task ID")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    args = parser.parse_args()

    # Database setup
    database = "todo.db"
    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")
        sys.exit(1)

    if args.add:
        add_task(conn, args.add)
    elif args.remove is not None:
        remove_task(conn, args.remove)
    elif args.mark_complete is not None:
        mark_task_completed(conn, args.mark_complete)
    elif args.list:
        list_tasks(conn)
    else:
        print("Use -h for help")
        sys.exit(0)

    conn.close()

if __name__ == '__main__':
    main()
