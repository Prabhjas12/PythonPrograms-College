tasks = []
def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added to the list.')
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed from the list.')
    else:
        print(f'Task "{task}" not found in the list.')
def list_tasks():
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")
while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        list_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
