from main_functions import cont, clear_screen
import random


def display_board(game_board):
    clear_screen()
    row_count = 1
    for row in game_board:
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if row_count < 3:
            print("----------")
            row_count += 1


def check_win_player(game_board, p_letter):
    for row in game_board:
        if all([spot == p_letter for spot in row]):

            display_board(game_board)
            return True

    if game_board[0][0] == p_letter and game_board[1][0] == p_letter and game_board[2][0] == p_letter or \
            game_board[0][1] == p_letter and game_board[1][1] == p_letter and game_board[2][1] == p_letter or \
            game_board[0][2] == p_letter and game_board[1][2] == p_letter and game_board[2][2] == p_letter:

        display_board(game_board)
        return True

    if game_board[0][0] == p_letter and game_board[1][1] == p_letter and game_board[2][2] == p_letter \
            or game_board[0][2] == p_letter and game_board[1][1] == p_letter and game_board[2][0] == p_letter:

        display_board(game_board)
        return True

    return False


def check_win_bot(game_board, b_letter):
    for row in game_board:
        if all([spot == b_letter for spot in row]):

            display_board(game_board)
            return True

    if game_board[0][0] == b_letter and game_board[1][0] == b_letter and game_board[2][0] == b_letter or \
            game_board[0][1] == b_letter and game_board[1][1] == b_letter and game_board[2][1] == b_letter or \
            game_board[0][2] == b_letter and game_board[1][2] == b_letter and game_board[2][2] == b_letter:

        display_board(game_board)
        return True

    if game_board[0][0] == b_letter and game_board[1][1] == b_letter and game_board[2][2] == b_letter \
            or game_board[0][2] == b_letter and game_board[1][1] == b_letter and game_board[2][0] == b_letter:

        display_board(game_board)
        return True

    return False


def check_tie(game_board):
    for row in game_board:
        for spot in row:
            if spot not in ['X', 'O']:
                return False
    return True


def player_turn(game_board, p_letter):
    while True:
        try:
            player_spot_picked = int(input("Enter the number where you want to go(1-9): "))

            if 1 <= player_spot_picked <= 9:
                row = (player_spot_picked - 1) // 3
                col = (player_spot_picked - 1) % 3

                if game_board[row][col] == player_spot_picked:
                    game_board[row][col] = p_letter
                    break

                else:
                    print("Spot is already taken. Choose an empty spot.")
                    cont()
                    continue

            else:
                print("Invalid number.")
                cont()
                continue

        except ValueError:
            print("Enter a number.")
            cont()
            display_board(game_board)
            continue


def bot_turn(game_board, b_letter):
    while True:
        bot_spot_picked = random.randint(1, 9)

        row = (bot_spot_picked - 1) // 3
        col = (bot_spot_picked - 1) % 3

        if game_board[row][col] == bot_spot_picked:
            game_board[row][col] = b_letter

            display_board(game_board)
            print(f"The bot played {bot_spot_picked}")
            cont()
            break

        else:
            continue


def play_again():
    while True:
        clear_screen()
        play_or_menu = input("Would you like to play again(Y or N): ").lower()
        if play_or_menu == 'y':
            return True
        elif play_or_menu == 'n':
            return False
        else:
            print("Invalid option.")
            cont()
