def display_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks):
    task_description = input("Enter task description: ")
    tasks.append(task_description)
    print("Task added successfully!")

def mark_completed(tasks):
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks.pop(task_index)
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def main():
    tasks = []

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
main()