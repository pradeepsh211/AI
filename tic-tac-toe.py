def show_board(board):
	"""Print the nine board squares as three rows."""
	for row in range(3):
		# Each row contains three consecutive positions from the board list.
		print(" | ".join(board[row * 3:row * 3 + 3]))
		if row < 2:
			print("---------")


def has_won(board, player):
	"""Return True when player occupies any complete row, column, or diagonal."""
	# Board positions are numbered left-to-right, top-to-bottom, from 0 to 8.
	lines = (
		(0, 1, 2), (3, 4, 5), (6, 7, 8),
		(0, 3, 6), (1, 4, 7), (2, 5, 8),
		(0, 4, 8), (2, 4, 6),
	)
	# A win occurs if every position in any winning line belongs to this player.
	return any(all(board[index] == player for index in line) for line in lines)


def play():
	"""Run a two-player game until someone wins or the board is full."""
	# Unplayed squares show their numbers so players can choose a position.
	board = [str(number) for number in range(1, 10)]
	player = "X"

	while True:
		# Show the latest board and ask the current player for a square.
		show_board(board)
		move = input(f"Player {player}, choose a square (1-9): ").strip()

		# Reject input outside 1-9 and squares that have already been played.
		if move not in "123456789" or len(move) != 1 or board[int(move) - 1] in ("X", "O"):
			print("Invalid move. Try again.")
			continue

		# Place the current player's mark in the selected square.
		board[int(move) - 1] = player
		if has_won(board, player):
			show_board(board)
			print(f"Player {player} wins!")
			break
		# If no empty numbered square remains, the game ends in a draw.
		if all(square in ("X", "O") for square in board):
			show_board(board)
			print("It's a draw!")
			break

		# Switch turns after a valid move that did not end the game.
		player = "O" if player == "X" else "X"


if __name__ == "__main__":
	# Start the game only when this file is run directly.
	play()
