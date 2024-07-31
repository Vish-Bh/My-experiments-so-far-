import keyboard
tasks = {}
 
def add_task(task_id, task_name):
    tasks[task_id] = {"name": task_name, "status": "pending"}
    print(f"Task '{task_name}' added with ID {task_id}!")

def update_task(task_id, new_name=None, new_status=None):
    if task_id in tasks:
        if new_name:
            tasks[task_id]["name"] = new_name
        if new_status:
            tasks[task_id]["status"] = new_status
        print(f"Task {task_id} updated!")
    else:
        print(f"Task {task_id} not found!")

def remove_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} removed!")
    else:
        print(f"Task {task_id} not found!")

def list_tasks():
    print("To-Do List:")
    for task_id, task in tasks.items():
        print(f"  {task_id}: {task['name']} ({task['status']})")

while True:
    print(tasks)
    print("\nOptions:")
    print("  1. Add task")
    print("  2. Update task")
    print("  3. Remove task")
    print("  4. List tasks")
    print("  5. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        task_id = input("Enter task ID: ")
        task_name = input("Enter task name: ")
        add_task(task_id, task_name)
    elif choice == "2":
        task_id = input("Enter task ID: ")
        new_name = input("Enter new task name (or press enter to skip): ")
        new_status = input("Enter new task status (or press enter to skip): ")
        update_task(task_id, new_name if new_name else None, new_status if new_status else None)
    elif choice == "3":
        task_id = input("Enter task ID: ")
        remove_task(task_id)
    elif choice == "4":
        list_tasks()
    elif choice == "5":
        break
    else:
        print("Invalid option. Try again!")
        print(help(11)) 
