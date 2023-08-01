import os
from termcolor2 import colored

def draw_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"   {board[1]}   |   {board[2]}   |   {board[3]}   ")
    print("-----------------------")
    print(f"   {board[4]}   |   {board[5]}   |   {board[6]}   ")
    print("-----------------------")
    print(f"   {board[7]}   |   {board[8]}   |   {board[9]}   ")

def get_player_choice(player):
    choice = int(input(f"Player '{player}', enter a number from 1 to 9: "))
    return choice

def check_win(board, player):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def tic_tac_toe():
    board = {i: " " for i in range(1, 10)}
    player1 = input("Enter symbol for Player 1 (X or O): ").upper()
    while player1 not in ["X", "O"]:
        player1 = input("Invalid symbol! Please enter 'X' or 'O': ").upper()
    player2 = "X" if player1 == "O" else "O"

    draw_board(board)

    for _ in range(9):
        current_player = colored(player1,"blue") if _ % 2 == 0 else colored(player2,"red")
        player_choice = get_player_choice(current_player)

        while board[player_choice] != " ":
            print("Invalid move! This position is already taken.")
            player_choice = get_player_choice(current_player)

        board[player_choice] = current_player
        draw_board(board)

        if _ >= 4:
            if check_win(board, current_player):
                print(f"Player '{current_player}' won!")
                break
        if _ == 8:
            print(colored("It's a tie!","yellow"))

if __name__ == "__main__":
    tic_tac_toe()
