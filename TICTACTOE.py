#board
import sys
import os
from os import system, name
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
table = ["-","-","-",
        "-","-","-",
        "-","-","-",]
count = 0
lis = []

def boardreset():
    for i in range(0,9):
        table[i] = "-"
    global count
    count  = 0

def check_row(table):
    for i in range(0,9,3):
        if table[i] == table[i+1] == table[i+2] and (table[i]=="X" or table[i] == "O"):
            print(table[i]+"WINS IN ROW")
            menu()

def check_col(table):
    for i in range(0,3):
        if table[i] == table[i+3] == table[i+6] and (table[i]=="X" or table[i] == "O"):
            print(table[i]+"WINS IN COLOUMN")
            menu()

def check_diag(table):
        if table[0] == table[4] == table[8] and (table[0] == "X" or table[0] == "O"):
            print(table[0]+" WINS IN DIAGONAL")
            menu()
        elif table[2] == table[4] == table[6] and (table[2] == "X" or table[2] == "O"):
            print(table[2]+" WINS IN DIAGONAL")
            menu()

def check_win(table):
    check_row(table)
    check_col(table)
    check_diag(table)

def handle_turn_o():
    print("ENTER THE POSTION FOR ' O' YOUR MARK(1-9)")
    x_pos = int(input())

    table[x_pos - 1] = "O"

def handle_turn_x():
    print("ENTER THE POSTION FOR ' X' YOUR MARK(1-9)")
    x_pos = int(input())
    table[x_pos - 1] = "X"

def check_full():
    global count
    count+=1
    if count < 9:
        return True
    else:
        print("GAME TIE")
        menu()

def display_board():
    print("---||-----||----")
    print(table[0] + "  ||  " + table[1] + "  ||  " + table[2])
    print("---||-----||----")
    print(table[3] + "  ||  " + table[4] + "  ||  " + table[5])
    print("---||-----||----")
    print(table[6] + "  ||  " + table[7] + "  ||  " + table[8])
    print("---||-----||----")

def handle_turn():
    x = True
    while x :
        handle_turn_x()
        clear()
        display_board()
        check_win(table)
        check_full()
        handle_turn_o()
        clear()
        display_board()
        check_win(table)
        check_full()
    handle_turn_x()
    check_win(table)


def display_board():
    print("---||-----||----")
    print(table[0] + "  ||  " + table[1] + "  ||  " + table[2])
    print("---||-----||----")
    print(table[3] + "  ||  " + table[4] + "  ||  " + table[5])
    print("---||-----||----")
    print(table[6] + "  ||  " + table[7] + "  ||  " + table[8])
    print("---||-----||----")

def play_game():
    display_board()
    handle_turn()
    print("GAME OVER")

def menu():
    print("1. START GAME\n2.END GAME")
    choice  = int(input("MAKE YOUR CHOICE"))
    clear()
    if choice == 1:
        boardreset()
        print("WELCOME ABOARD")
        play_game()
    else:
        print("THANK YOU")
        sys.exit()
menu()
