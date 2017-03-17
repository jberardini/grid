def test():


	j = 0
	random_variable = False

	while j < 5:
		print "I am j"
		print j
		print "\n"
		if not random_variable:
			i = 0

		random_variable = False
		while i < 5:
			print "I am i"
			print i 
			print "\n"
			

			if i == 3 and j == 3:

				i = 1
				j = 1
				random_variable = True
				break

			else:
				i += 1

		if not random_variable:
			j += 1

test()

#how to break out of an inner while loop?