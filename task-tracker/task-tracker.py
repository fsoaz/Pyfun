# Adding a new task
    # Output: Task added successfully (ID: 1)
# Updating and deleting tasks
# Marking a task as in progress or done
# Listing all tasks
# Listing tasks by status

# Inicial tasks list
# Initial tasks list
tasks = []
task_id_counter = 1

def displayTask(all_tasks):
    print("\nYour Tasks:")
    if len(all_tasks) == 0:
        print("No tasks found!")
    else:
        for task in all_tasks:
            print(
                f"{task['id']}. {task['title']} "
                f"[{task['status']}]"
                )

def addTask(all_tasks):
    global task_id_counter
    new_task = input("Add a task: ")
    task = {
        "id": task_id_counter,
        "title": new_task,
        "status": "Pending"
    }
    all_tasks.append(task)
    print(f"Task added successfully (ID: {task_id_counter})")
    task_id_counter += 1


def removeTask(all_tasks):
    displayTask(all_tasks)
    task_number = input("Enter the number of the task to remove: ")

    if task_number.isdigit():
        task_id = int(task_number)
        for task in all_tasks:
            if task["id"] == task_id:
                all_tasks.remove(task)
                print(f"Task '{task['title']}' removed!")
                return
            print("Task ID not found.")
        else:
            print("Please enter a valid number.")

def editTask(all_tasks):
    displayTask(all_tasks)
    task_number = input("Enter the number of the task to edit: ")

    if task_number.isdigit():
        task_id = int(task_number)
        for task in all_tasks:
            if task["id"] == task_id:
                new_text = input("Enter new task description: ")
                task["title"] = new_text
                print("Task updated successfully!")
                return
            print("Task ID not found")
        else:
            print("Please enter a valid number.")

def updateStatus(all_tasks):
    displayTask(all_tasks)
    task_number = input("Enter the ID of the task to update status: ")

    if task_number.isdigit():
        task_id = int(task_number)
        for task in all_tasks:
            if task["id"] == task_id:
                status = input(
                    "Enter status (pending / in progress / done): "
                ).lower()
                if status in ["pending", "in progress", "done"]:
                    task["status"] = status.title()
                    print("task status updated!")
                else:
                    print("Invalid status.")
                    return
                print("Task ID not found.")
            else:
                print("Please enter a valid number.")

def listByStatus(all_tasks):
    status = input("Enter status to filter (pending / in progress / done): ").lower()

    filtered = [t for t in all_tasks if t["status"].lower() == status]
    if not filtered:
        print(f"No tasks with status '{status}'.")
    else:
        displayTask(filtered)

def newOperation(all_tasks):
    while True:
        operation = input(
            "\nPress A to add, E to edit, R to remove, S to update status, L to list by status or Q to quit: "
        ).upper()

        if operation == 'A':
            addTask(all_tasks)
        elif operation == 'E':
            editTask(all_tasks)
        elif operation == 'R':
            removeTask(all_tasks)
        elif operation == 'S':
            updateStatus(all_tasks)
        elif operation == 'L':
            listByStatus(all_tasks)
        elif operation == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

# Start application
newOperation(tasks)
