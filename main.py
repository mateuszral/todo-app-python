from datetime import datetime


def print_menu():
    print("Choose one:")
    print("1. Display Tasks")
    print("2. Add task")
    print("3. Check task as completed")
    print("4. Exit")


def print_tasks(tasks):
    print("\nYour tasks:")
    for index, task in enumerate(tasks):
        print(
            f"{index + 1}. {task["description"]} {task["deadline"]} {"✅" if task["is_completed"] else ""}"
        )

def is_date_valid(date):
    if date == "":
        return True
    try:
        date = datetime.strptime(date, "%d-%m-%y")
        return date < datetime.now()
    except ValueError:
        return False

# boilerplate
tasks = [
    {
        "id": 1,
        "description": "Buy milk and groceries",
        "is_completed": False,
        "deadline": "20-01-2026",
    },
    {
        "id": 2, 
        "description": "Walk the dog", 
        "is_completed": True,
        "deadline": "",
    },
    {
        "id": 3,
        "description": "Read a book",
        "is_completed": False,
        "deadline": "30-01-2026",
    },
]

print("Welcome to the To-Do List application!\n")
print_menu()
choice = int(input("Enter your choice: "))

while choice != 4:
    match choice:
        case 1:
            print_tasks(tasks)
        case 2:
            new_task_description = input("Enter task name: ")
            
            if new_task_description.strip() == "":
                print("\nTask description cannot be empty. Task not added.\n")
                print_menu()
                
                choice = int(input("Enter your choice: "))
                continue
            
            new_task_deadline = input("Enter deadline (optional) [DD-MM-YY]: ")
            
            if not is_date_valid(new_task_deadline):
                print(f"\nInvalid date (format / past date). Task not added.\n")
                print_menu()
                
                choice = int(input("Enter your choice: "))
                continue
            
            tasks.append(
                {
                    "id": len(tasks) + 1,
                    "description": new_task_description.capitalize(),
                    "is_completed": False,
                    "deadline": new_task_deadline,
                }
            )
            
            print("\nTask added successfully")
            print_tasks(tasks)
        case 3:
            task_id = int(input("Enter number of the completed task: "))
            tasks[task_id - 1].update({"is_completed": True})
            
            print(f"\nTask no. {task_id} completed")
            print_tasks(tasks)
    print()
    print_menu()
    choice = int(input("Enter your choice: "))

print("\nThank you for using the To-Do List application. Goodbye!")
exit()
    