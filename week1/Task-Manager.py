# Deff + List

tasks = ["Study Python", "Practice Git", "Read AI Article"]

def show_tasks():
    for task in tasks:
        print("Your tasks:", "-", task)

def add_task(task):
    tasks.append(task)
    print("Task added!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed!")
    else:
        print("Task does not exist!")

show_tasks()
add_task("Go for a walk")
remove_task("Practice Git")
show_tasks()


# Task Manager

tasks = []

def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed!")
    else:
        print("Task does not exist!")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your tasks:", "-", tasks)

while True:
    show_menu()
    choice = input('Choose an option: ')
    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice!")