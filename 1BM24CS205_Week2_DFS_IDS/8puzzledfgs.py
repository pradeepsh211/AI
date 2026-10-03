GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def solve_dfs(start):
	stack, parent = [start], {start: None}
	while stack:
		state = stack.pop()
		if state == GOAL:
			path = []
			while parent[state]:
				previous, move = parent[state]
				path.append((move, state))
				state = previous
			return path[::-1]

		blank = state.index(0)
		row, column = divmod(blank, 3)
		for move, allowed, target in (
			("Up", row > 0, blank - 3), ("Left", column > 0, blank - 1),
			("Right", column < 2, blank + 1), ("Down", row < 2, blank + 3),
		):
			if allowed:
				next_state = list(state)
				next_state[blank], next_state[target] = next_state[target], next_state[blank]
			next_state = tuple(next_state)
			if next_state not in parent:
				parent[next_state] = (state, move)
				stack.append(next_state)
	return None


def print_board(state):
	for i in range(0, 9, 3):
		print(*(value or "_" for value in state[i:i + 3]))


if __name__ == "__main__":
	print("Enter the initial board row by row (use 0 for the blank):")
	rows = [input(f"Row {i + 1}: ").split() for i in range(3)]
	try:
		start = tuple(int(value) for row in rows for value in row)
		if any(len(row) != 3 for row in rows) or set(start) != set(range(9)):
			raise ValueError
	except ValueError:
		print("Enter three rows containing 0 through 8 exactly once.")
		raise SystemExit

	if sum(start[i] > start[j] for i in range(9) for j in range(i + 1, 9)
		   if start[i] and start[j]) % 2:
		print("This board cannot reach the goal.")
		raise SystemExit

	solution = solve_dfs(start)
	if solution is None:
		print("No solution found.")
	else:
		print(f"Solution found in {len(solution)} moves:")
		print_board(start)
		for move, state in solution:
			print()
			print(f"Move blank {move}:")
			print_board(state)
