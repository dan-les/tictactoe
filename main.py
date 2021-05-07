#!/usr/bin/python3
# Daniel Leśniewicz
import os
import random
import sys
import time


def choose_symbol():
    player = input("Wybierz swój symbol: 'X' lub 'O' ")
    player = player.upper()
    while True:
        if player == 'X':
            computer_symbol_o = 'O'
            return player, computer_symbol_o
        elif player == 'O':
            computer_symbol_x = 'X'
            return player, computer_symbol_x
        else:
            player = input("Możesz wybrać tylko 'X' lub 'O' ")
            player = player.upper()


def check_if_someone_win_a_game(new_board_cords, symbol):
    print(new_board_cords)
    if new_board_cords[0] == new_board_cords[1] == new_board_cords[2] == symbol or \
            new_board_cords[3] == new_board_cords[4] == new_board_cords[5] == symbol or \
            new_board_cords[6] == new_board_cords[7] == new_board_cords[8] == symbol or \
            new_board_cords[0] == new_board_cords[3] == new_board_cords[6] == symbol or \
            new_board_cords[1] == new_board_cords[4] == new_board_cords[7] == symbol or \
            new_board_cords[2] == new_board_cords[5] == new_board_cords[8] == symbol or \
            new_board_cords[0] == new_board_cords[4] == new_board_cords[8] == symbol or \
            new_board_cords[6] == new_board_cords[4] == new_board_cords[2] == symbol:
        return True
    return False


def cord_choice(board_coordinates, if_computer):
    if if_computer:
        rand = random.randint(0, 8)
        while board_coordinates[int(rand)] != '_':
            rand = random.randint(0, 8)
        return rand
    else:
        choice = input("Podaj miejsce do wstawienia symbolu: ")
        if board_coordinates[int(choice) - 1] != '_':
            print("Miejsce już zajęte!!!")
            cord_choice(board_coordinates, False)
        return int(choice) - 1


BOARD_WITH_CORDS = ("         P L A N S Z A         \n"
                    "###############################\n"
                    "#         #         #         #\n"
                    "#    1    #    2    #    3    #\n"
                    "#         #         #         #\n"
                    "###############################\n"
                    "#         #         #         #\n"
                    "#    4    #    5    #    6    #\n"
                    "#         #         #         #\n"
                    "###############################\n"
                    "#         #         #         #\n"
                    "#    7    #    8    #    9    #\n"
                    "#         #         #         #\n"
                    "###############################\n")


def display_board_with_symbols(board_cords_to_process):
    new_board = BOARD_WITH_CORDS

    for index in range(0, 9):
        if board_cords_to_process[index] == '_':
            new_board = new_board.replace(str(index + 1), ' ')
        else:
            new_board = new_board.replace(str(index + 1), board_cords_to_process[index])

    print(new_board)


if __name__ == "__main__":
    print('GRA - Kółko i Krzyżyk')
    player_symbol, computer_symbol = choose_symbol()
    i = 0
    board_cords = ['_'] * 9
    print("Numeracja pól:")
    print(BOARD_WITH_CORDS)

    while True:
        if i % 2 == 0:
            SYMBOL = player_symbol
            COMPUTER = False
        else:
            print("Komputer myśli (｡◕‿‿◕｡)")
            time.sleep(random.randint(2, 3))
            SYMBOL = computer_symbol
            COMPUTER = True

        position = cord_choice(board_cords, COMPUTER)
        os.system('cls')
        board_cords[position] = SYMBOL
        display_board_with_symbols(board_cords)
        i += 1

        if check_if_someone_win_a_game(board_cords, computer_symbol):
            print("Przegrałeś! ᕙ(⇀‸↼‶)ᕗ")
            sys.exit(0)
        if check_if_someone_win_a_game(board_cords, player_symbol):
            print("Wygrałeś! (ʘ‿ʘ)")
            sys.exit(0)
        if i == 9:
            print("Nikt nie wygrał! (￣෴￣)")
            sys.exit(0)
