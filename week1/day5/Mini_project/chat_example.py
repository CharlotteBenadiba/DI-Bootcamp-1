def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("___" * 9)

def check_winner(board, mark):
    # Check rows, columns, and diagonals for a winning condition
    for i in range(3):
        if all([board[i][j] == mark for j in range(3)]) or all([board[j][i] == mark for j in range(3)]):
            return True
    if all([board[i][i] == mark for i in range(3)]) or all([board[i][2 - i] == mark for i in range(3)]):
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    turn = 0
    while True:
        row = int(input("Player X, choose row (0-2): "))
        col = int(input("Player X, choose column (0-2): "))

        if board[row][col] != " ":
            print("That spot is already taken!")
            continue
        board[row][col] = "X"
        print_board(board)
        
        if check_winner(board, "X"):
            print("Player X wins!")
            break

        turn += 1
        if turn == 9:
            print("It's a tie!")
            break

        row = int(input("Player O, choose row (0-2): "))
        col = int(input("Player O, choose column (0-2): "))

        if board[row][col] != " ":
            print("That spot is already taken!")
            continue
        board[row][col] = "O"
        print_board(board)
        
        if check_winner(board, "O"):
            print("Player O wins!")
            break

        turn += 1
        if turn == 9:
            print("It's a tie!")
            break

play_game()