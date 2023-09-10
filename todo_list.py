from main_functions import cont, empty_list, clear_screen


def view_tasks(file_handler):
    file_handler.seek(0)
    tasks = file_handler.readlines()
    completed = []

    if not tasks:
        empty_list()
    else:
        index_counter = 1
        incomplete_exists = False

        for index, task in enumerate(tasks, start=0):
            task_parts = tasks[index].strip().split(" | ")
            task_completion = task_parts[0]
            task_description = task_parts[1]

            if task_completion == "Incomplete":
                print(f"{index_counter}. {task_completion} | {task_description}")
                index_counter += 1
                incomplete_exists = True
            else:
                completed.append(f"{task_completion} | {task_description}")

        if incomplete_exists:
            print()

        if completed:
            for task in completed:
                print(f"{index_counter}. {task.strip()}")
                index_counter += 1
            print()

        cont()


def add_task(file_handler):
    task = input("Enter new task: ")
    file_handler.write(f"Incomplete | {task}\n")
    print("Task added successfully.\n")
    cont()


def del_task(file_handler):
    file_handler.seek(0)
    tasks = file_handler.readlines()

    if not tasks:
        empty_list()
        return

    clear_screen()
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")

    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            file_handler.seek(0)
            file_handler.truncate()
            file_handler.writelines(tasks)

            print(f"\nTask #{task_index + 1} deleted successfully.")
        else:
            print("Invalid index, no task deleted.")
    except ValueError:
        print("Invalid input, no task deleted.")
    cont()


def com_task(file_handler):
    file_handler.seek(0)
    tasks = file_handler.readlines()

    if not tasks:
        empty_list()
        return

    clear_screen()
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")

    try:
        task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            task_parts = tasks[task_index].strip().split(" | ")
            task_completion = task_parts[0]
            task_description = task_parts[1]

            if task_completion == "Incomplete":
                tasks[task_index] = f"Completed | {task_description}\n"
                file_handler.seek(0)
                file_handler.truncate()
                file_handler.writelines(tasks)
                print(f"\nTask #{task_index + 1} marked as completed.")
            else:
                print(f"\nTask #{task_index + 1} is already marked as completed.")
        else:
            print("Invalid index, no task marked.")
    except ValueError:
        print("Invalid input, no task marked.")
    cont()
