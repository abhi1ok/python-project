# todo.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Deleted task: {task}")
    else:
        print(f"Task '{task}' not found.")

def list_tasks():
    print("Remaining tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

if __name__ == "__main__":
    while True:
        command = input("Enter command (add/delete/list/quit): ").lower()

        if command == "add":
            task = input("Enter task: ")
            add_task(task)
        elif command == "delete":
            task = input("Enter task to delete: ")
            delete_task(task)
        elif command == "list":
            list_tasks()
        elif command == "quit":
            break
        else:
            print("Invalid command. Try again.")
