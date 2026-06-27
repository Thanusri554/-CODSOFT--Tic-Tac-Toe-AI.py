import math

# Initialize board
board = [[" " for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
    print("-"*5)

# Check winner
def is_winner(board, player):
    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Check draw
def is_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Get available moves
def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, isMaximizing):
    if is_winner(board, "O"): return 1
    if is_winner(board, "X"): return -1
    if is_draw(board): return 0

    if isMaximizing:  # AI's turn
        bestScore = -math.inf
        for (i, j) in available_moves(board):
            board[i][j] = "O"
            score = minimax(board, depth+1, alpha, beta, False)
            board[i][j] = " "
            bestScore = max(bestScore, score)
            alpha = max(alpha, bestScore)
            if beta <= alpha: break
        return bestScore
    else:  # Human's turn
        bestScore = math.inf
        for (i, j) in available_moves(board):
            board[i][j] = "X"
            score = minimax(board, depth+1, alpha, beta, True)
            board[i][j] = " "
            bestScore = min(bestScore, score)
            beta = min(beta, bestScore)
            if beta <= alpha: break
        return bestScore

# Best move for AI
def best_move(board):
    bestScore = -math.inf
    move = None
    for (i, j) in available_moves(board):
        board[i][j] = "O"
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[i][j] = " "
        if score > bestScore:
            bestScore = score
            move = (i, j)
    return move

# Game loop
def play_game():
    while True:
        print_board(board)

        # Human move
        x, y = map(int, input("Enter row and col (0-2): ").split())
        if board[x][y] == " ":
            board[x][y] = "X"
        else:
            print("Invalid move, try again")
            continue

        if is_winner(board, "X"):
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("Draw!")
            break

        # AI move
        i, j = best_move(board)
        board[i][j] = "O"

        if is_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("Draw!")
            break

# Run the game
play_game()
