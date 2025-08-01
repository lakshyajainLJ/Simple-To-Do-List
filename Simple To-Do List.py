import json
from datetime import datetime

FILENAME = "todo_list.json"

def load_tasks():
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=2)

def show_menu():
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        due = f" (Due: {task['due']})" if task["due"] else ""
        print(f"{i}. [{status}] {task['title']}{due}")

def add_task(tasks):
    title = input("Enter task title: ").strip()
    due_date = input("Enter due date (optional, YYYY-MM-DD): ").strip()
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Skipping due date.")
            due_date = ""
    if title:
        tasks.append({"title": title, "done": False, "due": due_date})
        print("Task added.")
    else:
        print("Task title cannot be empty.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed: '{removed['title']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print(f"Marked '{tasks[num - 1]['title']}' as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
