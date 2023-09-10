import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def cont():
    input("Press Enter to continue...")
    print()


def print_menu():
    clear_screen()
    menu_options = [
        'To Do List',
        'Tic Tac Toe',
        'Exit']

    for index, option in enumerate(menu_options, start=1):
        print(f"{index}. {option}")


def print_todo_menu():
    clear_screen()
    todo_options = [
        'View Tasks',
        'Add Task',
        'Remove Task',
        'Mark Completed',
        'Main Menu'
    ]

    for index, option in enumerate(todo_options, start=1):
        print(f"{index}. {option}")


def empty_list():
    print("Your to-do list is empty.")
    cont()
