def display_board(board):
    # Display the Tic-Tac-Toe board
    print("\n" + board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8] + "\n")


def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    return (
        (board[0] == board[1] == board[2] == player) or
        (board[3] == board[4] == board[5] == player) or
        (board[6] == board[7] == board[8] == player) or
        (board[0] == board[3] == board[6] == player) or
        (board[1] == board[4] == board[7] == player) or
        (board[2] == board[5] == board[8] == player) or
        (board[0] == board[4] == board[8] == player) or
        (board[2] == board[4] == board[6] == player)
    )


def is_board_full(board):
    # Check if the board is full
    return ' ' not in board


def get_player_choice(board):
    # Get the player's move choice
    while True:
        try:
            choice = int(input("Enter your move (1-9): ")) - 1
            if choice in range(9) and board[choice] == ' ':
                return choice
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")


def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'
    winner = None

    print("Welcome to Tic-Tac-Toe!")

    while not winner:
        display_board(board)
        move = get_player_choice(board)

        board[move] = current_player

        if check_winner(board, current_player):
            display_board(board)
            winner = current_player
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


tic_tac_toe()
