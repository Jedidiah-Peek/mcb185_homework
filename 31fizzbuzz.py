for a in range(1, 101):
	output = a
	if a % 3 == 0: 
		output = 'Fizz'
	if a % 5 == 0: 
		if type(output) == int: output = 'Buzz'
		else:                   output = output +'Buzz'
	print(output)