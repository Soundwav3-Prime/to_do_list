import json

def load_tasks(filename):
    """Load tasks from a file in JSON format."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(filename, task_list):
    """Save tasks to a file in JSON format."""
    with open(filename, "w") as file:
        json.dump(task_list, file, indent=4)

def show_tasks(task_list):
    """Displays all tasks with details."""
    print("\nTo-Do List:")
    if not task_list:
        print("No tasks available.")
        return

    for i, task in enumerate(task_list, 1):
        print(f"{i}. {task['description']} (Due: {task['due']}, Priority: {task['priority']}, Category: {task['category']})")

def add_task(task_list):
    """Adds a new task with details."""
    description = input("Enter task description: ")
    due = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (high, medium, low): ").lower()
    category = input("Enter category (work, personal, etc.): ")

    new_task = {
        "description": description,
        "due": due,
        "priority": priority,
        "category": category
    }
    task_list.append(new_task)
    save_tasks("tasks.json", task_list)  # Save immediately
    print("✅ Task added successfully!")

def edit_task(task_list):
    """Allow the user to edit an existing task."""
    try:
        task_number = int(input("Enter the task number you want to edit: ")) - 1
        if 0 <= task_number < len(task_list):
            task = task_list[task_number]

            print(f"Editing task: {task['description']}")
            task["description"] = input(f"New description (leave blank to keep '{task['description']}'): ") or task["description"]
            task["due"] = input(f"New due date (leave blank to keep '{task['due']}'): ") or task["due"]
            task["priority"] = input(f"New priority (leave blank to keep '{task['priority']}'): ") or task["priority"]
            task["category"] = input(f"New category (leave blank to keep '{task['category']}'): ") or task["category"]

            save_tasks("tasks.json", task_list)  # Save after editing
            print("✅ Task updated successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def completed_task(task_list, completed_list):
    """Marks a task as complete and moves it to the completed list."""
    try:
        task_number = int(input("Enter the task number you completed: ")) - 1
        if 0 <= task_number < len(task_list):
            completed_task = task_list.pop(task_number)
            completed_list.append(completed_task)
            print(f"✅ Task '{completed_task['description']}' marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def show_complete(done_list):
    """Displays the list of completed tasks."""
    print("\nCompleted Tasks:")
    if done_list:
        for i, task in enumerate(done_list, 1):
            print(f"{i}. {task['description']}")
    else:
        print("No tasks completed yet.")

def removal(remove_task):
    """Remove tasks in lists"""
    try:
        if remove_task:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(remove_task):
                remove_task.pop(task_number - 1)
            else:
                print("Invalid task number.")
        else:
            print ("There are no tasks available to delete. Please add a task")
    except ValueError:
        print("Please enter a valid number.")