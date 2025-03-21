import task_manager

# Load tasks from files when the program starts
tasks = task_manager.load_tasks("tasks.json")
completed_tasks = task_manager.load_tasks("completed_tasks.json")  # Load completed tasks

while True:
    task_manager.show_tasks(tasks)

    print("\nOptions:")
    print("1 - Add Task")
    print("2 - Edit Task")
    print("3 - Mark Task as Complete")
    print("4 - Show Completed Tasks")
    print("5 - Remove Task")
    print("6 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task_manager.add_task(tasks)
    
    elif choice == "2":
        task_manager.edit_task(tasks)
    
    elif choice == "3":
        task_manager.completed_task(tasks, completed_tasks)  # Corrected
    
    elif choice == "4":
        task_manager.show_complete()  # No argument needed
    
    elif choice == "5":
        task_manager.removal(tasks)
    
    elif choice == "6":
        task_manager.save_tasks("tasks.json", tasks)
        task_manager.save_tasks("completed_tasks.json", completed_tasks)  # Save completed tasks
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
