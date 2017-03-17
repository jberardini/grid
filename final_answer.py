def get_paths(size, obstacles, jumps):

	height, width = size

	paths = [[None for _ in range(width)] for _ in range(height)]

	jump_lookup = {}

	for jump_from, jump_to in jumps:
		jump_lookup[jump_from] = jump_to

	already_updated = set()

	for obstacle in obstacles:
		obstacle_y, obstacle_x = obstacle
		paths[obstacle_y][obstacle_x] = 0
		already_updated.add((obstacle_y, obstacle_x))

	current_y = 0

	jumped = False

	to_return_to = {}


	while current_y < height:


		if not jumped:
			current_x = 0

		jumped = False

		while current_x < width:

			if (current_y,current_x) not in already_updated:

				if (current_y,current_x) in jump_lookup:

					jump_to_y, jump_to_x = jump_lookup[(current_y,current_x)]

					if not paths[jump_to_y][jump_to_x]:
						to_return_to[(jump_to_y,jump_to_x)] = (current_y,current_x)
						paths[current_y][current_x] = calculate_paths(paths,current_y,current_x)


					else:
						moves_to_date = calculate_paths(paths,current_y,current_x)
						paths[current_y][current_x] = 0
						already_updated.add((current_y, current_x))
						
						paths[jump_to_y][jump_to_x] += moves_to_date
						current_y = jump_to_y
						current_x = jump_to_x + 1

						jumped = True
						break



				elif (current_y,current_x) in to_return_to:

					moves_to_date = calculate_paths(paths,current_y,current_x)

					jump_from_y, jump_from_x = to_return_to[(current_y,current_x)]
					additional_moves = paths[jump_from_y][jump_from_x]
					paths[current_y][current_x] = moves_to_date + additional_moves

					already_updated.add((current_y,current_x))

					paths[jump_from_y][jump_from_x] = 0

					del to_return_to[(current_y,current_x)]

					current_y = jump_from_y
					current_x = jump_from_x + 1

					jumped = True

					break


				else:
					paths[current_y][current_x] = calculate_paths(paths,current_y,current_x)

			if not jumped:
				current_x += 1

		if not jumped:
			current_y += 1

	return paths[height-1][width-1]


def calculate_paths(paths, i, j):

	if i == 0 and j == 0:
		paths[i][j] = 1

	elif i == 0:
		paths[i][j] = paths[i][j-1]

	elif j == 0:
		paths[i][j] = paths[i-1][j]

	else:
		paths[i][j] = paths[i-1][j] + paths[i][j-1]


	return paths[i][j]

print get_paths((5,5), [(2,2)], [((2,1), (0,3)), ((2,3), (0,0))])

# print get_paths((2,2), [], [])

# print get_paths((5,5), [(0,0)], [])

# print get_paths((5,5), [], [((0,3), (2,1))])






