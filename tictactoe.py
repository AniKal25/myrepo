# Anita Barbra Kalu
# 14th January, 2022
# CSE 210

print()
print("This is a Tic Tac Toe Game")
print()

print("Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row,\n a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.")

def main():
    player = later_player("")
    board = make_board()
    while not (is_winner(board) or is_draw(board)):
        show_board(board)
        make_move(player, board)
        player = later_player(player)
    show_board(board)
    print("Fantastic game. Thanks for playing!") 

def make_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def show_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def is_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
def is_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player


def later_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()