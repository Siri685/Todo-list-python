def show_tasks(tasks):
    if not tasks:
        print("No tasks in your list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def main():
    tasks = []

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks.pop(num - 1)
                print(f"Removed task: {removed}")
            except (ValueError, IndexError):
                print("Invalid task number!")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()