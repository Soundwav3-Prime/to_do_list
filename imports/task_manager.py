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
        if task_number < 0 or task_number >= len(task_list):
            raise IndexError("❌ Task number is out of range")
        
        task = task_list[task_number]

        print(f"Editing task: {task['description']}")
        task["description"] = input(f"New description (leave blank to keep '{task['description']}'): ") or task["description"]
        task["due"] = input(f"New due date (leave blank to keep '{task['due']}'): ") or task["due"]
        task["priority"] = input(f"New priority (leave blank to keep '{task['priority']}'): ") or task["priority"]
        task["category"] = input(f"New category (leave blank to keep '{task['category']}'): ") or task["category"]

        save_tasks("tasks.json", task_list)  # Save after editing
        print("✅ Task updated successfully!")
    except ValueError:
        print("❌ Please enter a valid number.")
    except IndexError as e:
        print(e)

def completed_task(task_list, completed_list):
    """Marks a task as complete and moves it to the completed list."""
    try:
        task_number = int(input("Enter the task number you completed: ")) - 1
        if task_number < 0 or task_number >= len(task_list):
            raise IndexError("❌ Task number is out of range.") # Raise an error manually
        completed_task = task_list.pop(task_number)
        completed_list.append(completed_task)
        save_tasks("tasks.json", task_list)
        print(f"✅ Task '{completed_task['description']}' marked as complete!")
    except ValueError:
        print("❌ Please enter a valid number.")
    except IndexError as e:
        print(e)

def show_complete(done_list):
    """Displays the list of completed tasks."""
    print("\nCompleted Tasks:")
    if done_list:
        for i, task in enumerate(done_list, 1):
            print(f"{i}. {task['description']}")
    else:
        print("No tasks completed yet.")

def removal(task_list):
    """Remove tasks in lists"""
    try:
        if task_list:
            task_number = int(input("Enter the task number to remove: ")) -1
            if task_number < 0 or task_number >= len(task_list):
                raise IndexError("❌ Task number is out of range.")
            
            removed_task = task_list.pop(task_number)
            save_tasks("tasks.json", task_list)
            print(f"✅ Task '{removed_task['description']}' removed.")
        else:
            print ("There are no tasks available to delete. Please add a task")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError as e:
        print(e)