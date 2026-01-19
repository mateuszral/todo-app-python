from datetime import datetime
import time

def print_menu():
    print("Choose one:")
    print("1. Display Tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task/s")
    print("5. Exit")


def print_tasks(tasks):
    print("\nYour tasks:")
    for index, task in enumerate(tasks):
        print(
            f"{index + 1}. {task['description']} {task['deadline']} {'✅' if task['is_completed'] else ''}"
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
        "description": "Buy milk and groceries",
        "is_completed": False,
        "deadline": "20-01-2026",
    },
    {
        "description": "Walk the dog", 
        "is_completed": True,
        "deadline": "",
    },
    {
        "description": "Read a book",
        "is_completed": False,
        "deadline": "30-01-2026",
    },
]

print("Welcome to the To-Do List application!\n")
print_menu()

try:
    choice = int(input("Enter your choice: "))
except ValueError:
    print("\nInvalid input. Please enter a number from 1 to 5.\n")
    choice = 0
    
while choice != 5:
    match choice:
        case 0:
            print()
            print_menu()
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("\nInvalid input. Please enter a number from 1 to 5.\n")
                choice = 0
        case 1:
            print_tasks(tasks)
            
            choice = 0
        case 2:
            new_task_description = input("Enter task name: ")
            
            if new_task_description == "0":
                choice = 0
                continue
            
            if new_task_description.strip() == "":
                print("\nTask description cannot be empty. Task not added. Type 0 to return to main menu\n")
                    
                continue
            
            if new_task_description.lower() in [task["description"].lower() for task in tasks]:
                print("\nTask already exists. Task not added.\n")
                
                choice = 0    
                continue
            
            new_task_deadline = input("Enter deadline (optional) [DD-MM-YY]: ")
            
            if not is_date_valid(new_task_deadline):
                print(f"\nInvalid date (format / past date). Task not added.\n")

                continue
            
            tasks.append(
                {
                    "description": new_task_description.capitalize(),
                    "is_completed": False,
                    "deadline": new_task_deadline,
                }
            )
            
            print("\nTask added successfully")
            print_tasks(tasks)
            choice = 0
        case 3:
            try:
                task_id = int(input("Enter number of the completed task: "))
            except ValueError:
                print("\nInvalid input. Please enter a valid task number.\n")
                print_tasks(tasks)
                
                choice = 3
                continue
            
            if task_id == "0":
                choice = 0
                continue
            
            if task_id < 0 or len(tasks) < task_id:
                print("\nTask does not exist. Please enter valid task number or type 0 to return to main menu\n")
                
                continue
            
            tasks[task_id - 1].update({"is_completed": True})
            
            print(f"\nTask no. {task_id} completed")
            print_tasks(tasks)
            choice = 0
        case 4:
            task_ids = input("Enter numbers of the task/s to delete (separated by commas) or type 'all' to delete everything (irreversible - type 0 to return to main menu): ").strip().lower()
            
            print_tasks(tasks)
            
            if task_ids == "0":
                choice = 0
                continue
            
            if task_ids == "all":
                tasks.clear()
                print("\nAll tasks deleted.\n")
            elif not task_ids.replace(",", "").strip().isdigit():
                print("\nInvalid input. Please enter valid task numbers separated by commas or 'all'.\n")
            elif task_ids == "":
                print("\nNo task IDs provided. No tasks deleted.\n")
            else:
                task_ids = [int(id.strip()) for id in task_ids.split(",")]
                
                print()
                
                for index, task_id in enumerate(sorted(task_ids)):   
                    if 0 < (task_id - index) <= len(tasks):
                        tasks.pop(task_id - 1 - index)
                        print(f"Task no. {task_id} deleted.")
                    else:
                        print(f"Task no. {task_id} does not exist. Skipping.")
                        
                print()
            choice = 0
        case _:
            print("\nInvalid choice. Please try again.\n")
            choice = 0
                

print("\nThank you for using the To-Do List application. Goodbye!")
time.sleep(2)
exit()
    