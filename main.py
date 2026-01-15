def print_menu():
    print("Choose one:")
    print("1. Display Tasks")
    print("2. Add task")
    print("3. Delete Task")
    print("4. Exit")


def print_tasks(tasks):
    print("\nYour tasks:")
    for index, task in enumerate(tasks):
        print(
            f"{index + 1}. {task['description']} {task["deadline"]} {'✅' if task['is_completed'] else ''}"
        )


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
            new_task_deadline = input("Enter deadline (optional) [DD-MM-YYYY]: ")
            
            tasks.append(
                {
                    "id": len(tasks) + 1,
                    "description": new_task_description.capitalize(),
                    "is_completed": False,
                    "deadline": new_task_deadline,
                }
            )
            
            print("\nTask added successfully")
        case 3:
            print("delete")
    print()
    print_menu()
    choice = int(input("Enter your choice: "))

exit()
