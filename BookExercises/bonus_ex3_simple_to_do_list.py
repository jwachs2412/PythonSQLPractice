tasks = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")
    
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
def remove_task():
    view_tasks()
    try:
        task_number= int(input("Enter the task number to remove: "))
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed}' removed!")
    except (IndexError, ValueError):
        print("Invalid task number.")
        
while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")