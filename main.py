import os
import random

board_with_cords = \
    """         P L A N S Z A    
###############################
#         #         #         #
#    1    #    2    #    3    #
#         #         #         #
###############################
#         #         #         #
#    4    #    5    #    6    #
#         #         #         #
###############################
#         #         #         #
#    7    #    8    #    9    #
#         #         #         #
###############################
"""


def display_board_with_symbols(board_cords):
    board_with_changed_cords = board_with_cords
    for i in range(1, 10):
        if board_cords[i] == '#':
            board_with_changed_cords = board_with_changed_cords.replace(str(i), ' ')
        else:
            board_with_changed_cords = board_with_changed_cords.replace(str(i), board_cords[i])

    print(board_with_changed_cords)


def check_if_someone_win_a_game(board_cords, symbol):
    if board_cords[1] == board_cords[2] == board_cords[3] == symbol:
        return True
    if board_cords[4] == board_cords[5] == board_cords[6] == symbol:
        return True
    if board_cords[7] == board_cords[8] == board_cords[9] == symbol:
        return True
    if board_cords[1] == board_cords[4] == board_cords[7] == symbol:
        return True
    if board_cords[2] == board_cords[5] == board_cords[8] == symbol:
        return True
    if board_cords[3] == board_cords[6] == board_cords[9] == symbol:
        return True
    if board_cords[4] == board_cords[5] == board_cords[7] == symbol:
        return True
    if board_cords[1] == board_cords[5] == board_cords[9] == symbol:
        return True
    return False


def cord_choice(board_cords, if_computer):

    if(if_computer):
        os.system('cls')
        return random.randint(1, 9)
    choice = input("Podaj miejsce do wstawienia symbolu: ")
    if board_cords[int(choice)] != '#':
        print("Miejsce już zajęte!!!")
        cord_choice(board_cords)
    os.system('cls')
    return int(choice)


def choose_symbol():
    player = input("Wybierz swój symbol: 'X' lub 'O' ")
    player = player.upper()
    while True:
        if player == 'X':
            computer = 'O'
            return player, computer
        elif player == 'O':
            computer = 'X'
            return player, computer
        else:
            player = input("Możesz wybrać tylko 'X' lub 'O' ")


if __name__ == "__main__":
    print('GRA - Kółko i Krzyżyk')
    player_symbol, computer_symbol = choose_symbol()
    i = 0
    board_cords = ['#'] * 10
    print("Numeracja pól:")
    print(board_with_cords)



    while True:
        if_computer = False
        if i % 2 == 0:
            symbol = player_symbol
        else:
            symbol = computer_symbol
            if_computer = True

        position = cord_choice(board_cords, if_computer)

        board_cords[position] = symbol
        display_board_with_symbols(board_cords)
        i += 1

        if check_if_someone_win_a_game(board_cords, symbol):
            print("Wygrałeś!")
            exit(0)
        if i == 9:
            print("Nikt nie wygrał!")
            exit(0)
