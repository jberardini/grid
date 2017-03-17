def number_of_paths(size):

	y = size[0]
	x = size[1]

	ways = [[None for _ in range(x)] for _ in range(y)]

	for i in range(y):

		for j in range(x):

			if i == 0 and j == 0:
				ways[i][j] = 1

			elif i == 0:
				ways[i][j] = ways[i][j-1]

			elif j == 0:
				ways[i][j] = ways[i-1][j]

			else:
				ways[i][j] = ways[i-1][j] + ways[i][j-1]


	return ways[y-1][x-1]

# print number_of_paths((2,2))
# print number_of_paths((3,3))
# print number_of_paths((4,4))
# print number_of_paths((5,5))

def get_paths(size):

	answer = 1
	y = size[0]
	x = size[1]

	for i in range(x, (y + x - 1)):
		answer *= i
		print "This is the first answer"
		print answer
		answer /= (i - x + 1)
		print "This is the second answer"
		print answer
		print '\n'

	return answer

# print "This is the answer to 2x2"
# print get_paths((2,2))
# print "\n"
# print "This is the answer to 5x5"
# print get_paths((5,5))

def another_get_paths(size):

	y = size[0]
	x = size[1]

	count = [[None for _ in range(x)] for _ in range(y)]

	for i in range(y):
		count[i][0] = 1

	print count

	for j in range(x):
		count[0][j] = 1

	print count

	for i in range(1, y):

		for j in range(1, x):

			count[i][j] = count[i-1][j] + count[i][j-1]

	print count

	return count[y-1][x-1]

# print another_get_paths((5,5))


def num_ways(size, obstacles, jumps):

	y = size[0]
	x = size[1]

	num_ways = [[None for _ in range(x)] for _ in range(y)]

	jump_lookup = {}

	for jump_from, jump_to in jumps:
		jump_lookup[jump_from] = jump_to 

	for obstacle in obstacles:
		m = obstacle[0]
		n = obstacle[1]
		num_ways[m][n] = False

	i = 0
	
	jumped = False
	

	while i < y:

		print "this is i"
		print i
		print "\n"

		if not jumped:
			j = 0

		jumped = False

		while j < x:

			print "this is j"
			print j
			print "\n"

			
			if num_ways[i][j] != False:


				if (i, j) in jump_lookup:	
					moves_to_date = num_ways[i-1][j] + num_ways[i][j-1]
					jump_to_y, jump_to_x = jump_lookup[(i, j)]
					num_ways[i][j] = False
					
					num_ways[jump_to_y][jump_to_x] += moves_to_date
					i = jump_to_y
					j = jump_to_x + 1

					jumped = True

					break

				else:
					if i == 0 and j == 0:
						num_ways[i][j] = 1

					elif i == 0:
						num_ways[i][j] = num_ways[i][j-1]

					elif j == 0:
						num_ways[i][j] = num_ways[i-1][j]
				


					#go back to the jump to point
					#add the jump from point to blocked points
					#change the for loops to while loops
					#hold the number of to ways in a varaible
					# add those to the number already at the jump to point
					#what happens if we haven't already seen that number? --> save for later
					#switch the order of the if statements so that this comes first? --> for now, just assume i and j won't be zero


					# if 


					else:
						num_ways[i][j] = num_ways[i-1][j] + num_ways[i][j-1]

					j += 1

			else:
				j += 1

		if not jumped:
			i += 1


	return num_ways[y-1][x-1]


# print num_ways((2,2), [], [])

print num_ways((5,5), [], [((2,1), (0,3))])
#so, what do we do if the jump to is after the jump from point

#if the number of ways to the jump to path haven't been defined yet
#wait until the number of ways have been defined
#then, go back to the jump from point, change ways to zero and add whatever ways was
#to the ways for the jump to point
#start iterating at the jump point and updating the ways except for the jump to point
#just skip calculating the jump to point

#blocked points in the first row or column are going to fuck things up
#maybe change Falses to 0? Or say if you hit a False, treat it like a zero

#edge case if the jump to or from point is at the first point
#if a blocked point is in the first row or column