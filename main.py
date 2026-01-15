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
            f"{index + 1}. {task['description']} {'✅' if task['is_completed'] else ''} {task.get('deadline', '')}"
        )
    print()


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
        "is_completed": True
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
            print()
            print_menu()
        case 2:
            print_tasks(tasks)
        case 3:
            print("delete")
    choice = int(input("Enter your choice: "))

exit()
