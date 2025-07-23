#task 1
#function to show tasks
tasks = []
def show_tasks():
    print("\nYour To-Do List:")
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

#function to add tasks in list
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

#function to remove any task
def remove_task():
    show_tasks()
    try:
        num = int(input("Enter the task number to remove: "))
        tasks.pop(num - 1)
        print("Task removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")
        
while True:
    print("\nTo-Do List Menu:")
    print("1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice.")
