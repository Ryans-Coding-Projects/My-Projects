todo_list = []

def add_task(task):
    todo_list.append(task)

def view_tasks():
    for task in todo_list:
        print(task)

def complete_task(task):
    todo_list.remove(task)

while True:
    print("\n1. Add task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("\nEnter you choice: ")

    if choice == "1":
        task = input("\nEnter the task: ")
        add_task(task)
        print("\nTask added succesfully")

    elif choice == "2":
        print("Your tasks are,")
        view_tasks()

    elif choice == "3":
        task = input("\nEnter the task to complete: ")
        complete_task(task)
        print("\nTask completed succefully")
        
    elif choice == "4":
        print("Thank for using the Python to-do list program")
        break

    else:
        print("\nInvalid Choice. Please enter a number between 1 and 4.")
    
        
