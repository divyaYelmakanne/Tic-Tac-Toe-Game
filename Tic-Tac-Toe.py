def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]

    for condition in win_conditions:
        if (board[condition[0]] == player and
            board[condition[1]] == player and
            board[condition[2]] == player):
            return True

    return False


def is_full(board):
    return all(cell != ' ' for cell in board)


def tic_tac_toe():
    board = [' '] * 9
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)

        player = players[turn % 2]

        try:
            position = int(input(f"Player {player}, choose a position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Please choose a number between 1 and 9.")
                continue

            if board[position] != ' ':
                print("That position is already taken!")
                continue

            board[position] = player

            if check_winner(board, player):
                print_board(board)
                print(f"🎉 Player {player} wins!")
                break

            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break

            turn += 1

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    tic_tac_toe()
