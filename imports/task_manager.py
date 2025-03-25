import json
from datetime import datetime

TASKS_FILE = "tasks.json"
COMPLETED_FILE = "completed_tasks.json"

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

def get_valid_date():
    """Prompt the user until they enter a valid date in MM-DD-YYYY."""
    while True:
        date_str= input("Enter due date (MM-DD-YYYY): ")
        try:
            valid_date = datetime.strptime(date_str, "%m-%d-%Y")
            return date_str
        except ValueError:
            print("❌ Invalid date format! Please enter in MM-DD-YYYY format.")

def new_valid_date(new_due_date):
    """Prompt the user until they enter a valid date in MM-DD-YYYY."""
    while True:
        try:
            valid_date = datetime.strptime(new_due_date, "%m-%d-%Y")
            return new_due_date
        except ValueError:
            print("❌ Invalid date format! Please enter in MM-DD-YYYY format.")

def add_task(task_list):
    """Adds a new task with details."""
    description = input("Enter task description: ").strip()
    while not description:
        print ("❌ Description cannot be empty!")
        description = input("Enter task description: ").strip()
        
    due = get_valid_date()
    
    priority = input("Enter priority (high, medium, low): ").lower()
    while priority not in ["high", "medium", "low"]:
        print("❌ Invalid priority! Choose from high, medium, or low.")
        priority = input("Enter priority (high, medium, low): ").lower()
        
    category = input("Enter category (work, personal, etc.): ")

    new_task = {
        "description": description,
        "due": due,
        "priority": priority,
        "category": category
    }
    task_list.append(new_task)
    save_tasks(TASKS_FILE, task_list)  # Save immediately
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
        
        new_due = input(f"New due date (leave blank to keep '{task['due']}'): ")
        if new_due:
            task["due"] = new_valid_date(new_due) if new_due else task["due"]
        
        new_priority = input(f"New priority (leave blank to keep '{task['priority']}'): ").lower()
        while new_priority and new_priority not in ["high", "medium", "low"]:
            print("❌ Invalid priority! Choose from high, medium, or low.")
            new_priority = input(f"New priority (leave blank to keep '{task['priority']}'): ").lower()
        task["priority"] = new_priority if new_priority else task["priority"]
        
        task["category"] = input(f"New category (leave blank to keep '{task['category']}'): ") or task["category"]

        save_tasks(TASKS_FILE, task_list)  # Save after editing
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
            raise IndexError("❌ Task number is out of range.") 
        completed_task = task_list.pop(task_number)
        completed_list.append(completed_task)
        save_tasks(TASKS_FILE, task_list)  # Save remaining tasks
        save_tasks(COMPLETED_FILE, completed_list)  # Save completed tasks
        print(f"✅ Task '{completed_task['description']}' marked as complete!")
    except ValueError:
        print("❌ Please enter a valid number.")
    except IndexError as e:
        print(e)

def show_complete(completed_list):
    """Load completed tasks from file."""
    return load_tasks(COMPLETED_FILE)

def show_complete():
    """Displays the list of completed tasks."""
    done_list = load_completed_tasks()
    print("\nCompleted Tasks:")
    if done_list:
        for i, task in enumerate(done_list, 1):
            print(f"{i}. {task['description']}")
    else:
        print("No tasks completed yet.")

def removal(task_list):
    """Remove tasks from the list."""
    try:
        if task_list:
            task_number = int(input("Enter the task number to remove: ")) -1
            if task_number < 0 or task_number >= len(task_list):
                raise IndexError("❌ Task number is out of range.")
            
            removed_task = task_list.pop(task_number)
            save_tasks(TASKS_FILE, task_list)
            print(f"✅ Task '{removed_task['description']}' removed.")
        else:
            print("There are no tasks available to delete. Please add a task")
    except ValueError:
        print("❌ Please enter a valid number.")
    except IndexError as e:
        print(e)
