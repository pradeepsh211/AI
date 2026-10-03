GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def depth_limited_search(state, depth, path_states):
	if state == GOAL:
		return []
	if depth == 0:
		return None

	blank = state.index(0)
	row, column = divmod(blank, 3)
	for move, allowed, target in (
		("Up", row > 0, blank - 3), ("Left", column > 0, blank - 1),
		("Right", column < 2, blank + 1), ("Down", row < 2, blank + 3),
	):
		if not allowed:
			continue
		next_state = list(state)
		next_state[blank], next_state[target] = next_state[target], next_state[blank]
		next_state = tuple(next_state)
		if next_state in path_states:
			continue

		path_states.add(next_state)
		solution = depth_limited_search(next_state, depth - 1, path_states)
		path_states.remove(next_state)
		if solution is not None:
			return [(move, next_state)] + solution
	return None


def solve_ids(start, max_depth=31):
	for depth in range(max_depth + 1):
		solution = depth_limited_search(start, depth, {start})
		if solution is not None:
			return solution
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

	solution = solve_ids(start)
	if solution is None:
		print("No solution found.")
	else:
		print(f"Solution found in {len(solution)} moves:")
		print_board(start)
		for move, state in solution:
			print()
			print(f"Move blank {move}:")
			print_board(state)
