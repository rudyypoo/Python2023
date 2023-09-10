from main_functions import cont, print_menu, print_todo_menu, clear_screen
from todo_list import view_tasks, add_task, del_task, com_task
from ttt_game import display_board, check_win_player, check_win_bot, check_tie, player_turn, bot_turn, play_again


def todo_picked(file_handler):
    while True:
        print_todo_menu()
        picked = input("Enter an option: ")
        print()

        if picked == "1":
            view_tasks(file_handler)
        elif picked == "2":
            add_task(file_handler)
        elif picked == "3":
            del_task(file_handler)
        elif picked == "4":
            com_task(file_handler)
        elif picked == "5":
            print("Returning to Main Menu.")
            cont()
            break
        else:
            print("Invalid option.")


def ttt_picked():
    game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    p_letter = None
    b_letter = None
    players_turn = False

    while True:
        clear_screen()
        print("TicTacToe\n---------")

        first_second = input("Will you go first or second (1 or 2): ")
        if first_second == "1":
            p_letter, b_letter = 'X', 'O'
            print(f"You will be {p_letter}'s.")
            players_turn = True
            cont()
            display_board(game_board)
            break
        elif first_second == "2":
            p_letter, b_letter = 'O', 'X'
            print(f"You will be {p_letter}'s.")
            cont()
            display_board(game_board)
            break
        else:
            print("Invalid option.")
            cont()
            continue

    while True:
        if players_turn:
            player_turn(game_board, p_letter)
            players_turn = False
        elif not players_turn:
            bot_turn(game_board, b_letter)
            players_turn = True

        if check_win_player(game_board, p_letter):
            print("Player Wins!")
            cont()
            break
        elif check_win_bot(game_board, b_letter):
            print("Bot Wins!")
            cont()
            break
        elif check_tie(game_board):
            print("The game is tied!")
            cont()
            break

    if play_again():
        ttt_picked()
    else:
        print("Returning to Main Menu.")
        cont()


if __name__ == "__main__":
    with open('todolist.txt', 'a+') as fh:
        while True:
            print_menu()
            option_picked = input("Enter an option: ")
            print()

            if option_picked == "1":
                todo_picked(fh)
            elif option_picked == "2":
                ttt_picked()
            elif option_picked == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid option.")
