todo_list = []


def show_menu():
    print("\n My To-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")


def add_task():
    task = input("Enter task: ")
    todo_list.append(task)
    print("Task added!")


def view_tasks():
    if len(todo_list) == 0:
        print("No tasks yet!")
    else:
        print("\nYour tasks:")
        for i in range(len(todo_list)):
            print(f"{i + 1}. {todo_list[i]}")


def remove_task():
    view_tasks()
    if len(todo_list) > 0:
        task_num = int(input("Enter task number to remove: "))
        if task_num > 0 and task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")


while True:
    show_menu()
    choice = input("\nChoose option (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
