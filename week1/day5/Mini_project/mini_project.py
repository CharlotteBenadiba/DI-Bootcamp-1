# board = [
#     ['col','col','col'
#     'col','col','col'
#      'col','col','col' ]
# ]

# def display_board(board):
#     print( '___' + board[0],[0] + '|' + '___ ' + board[0],[1] + '|' + '___ ' + board[0],[2] + '|'
#           '___ ' + board[1],[0] + '|'+ '___ ' + board[1],[1] + '|' + '___ ' + board[1],[2] + '|'
#           '___ ' + board[2],[0] + '|'+ '___ ' + board[2],[1] + '|' + '___ ' + board[2],[2] + '|')
# display_board(board)    


# position = int(input('choose position (1 - 9): '))
# board[0][position-1] = 'X'
# print(board)    

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 9)    

def check_win(board, mark):
    for i in range(3):
        if all([board[i][j] == mark for j in range(3)]) or all([board[j][i] == mark for j in range(3)]):
            return True
    if all([board[i][i] == mark for i in range(3)]) or all([board[i][2 - i] == mark for i in range(3)]):
        return True
    return False        

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    display_board(board)
    
    turn = 0
    while True:
        row = int(input("Player X, choose row (0-2): "))
        col = int(input("Player X, choose column (0-2): "))

        if board[row][col] != " ":
            print("That spot is already taken!")
            continue
        board[row][col] = "X"
        display_board(board)
        
        if check_win(board, "X"):
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
        display_board(board)
        
        if check_win(board, "O"):
            print("Player O wins!")
            break

        turn += 1
        if turn == 9:
            print("It's a tie!")
            break

play()