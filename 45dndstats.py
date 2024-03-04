import random


method_1 = 0
method_2 = 0
method_3 = 0
method_4 = 0


for a in range(100000):
	lowest = random.randint(1,6)   # first roll of 4D6d1
	for b in range(3):
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		method_1 += d1             # add result of roll to 3d6
		if d1 != 1:                # check if there is a 1 and then add result/reroll
			method_2 += d1
		else:
			method_2 += d2
		if d1 >= d2:               # add higher of 2 rolls to 3d6x2
			method_3 += d1
		else:
			method_3 += d2
		if d1 >= lowest:           # check if roll is higher than lowest thus far
			method_4 += d1
		else:                      # if roll is lowest add prevous lowest and save result
			method_4 += lowest
			lowest = d1


print(f'3D6 average = {method_1 / 100000}')
print(f'3D6r1 average = {method_2 / 100000}')
print(f'3D6x2 average = {method_3 / 100000}')
print(f'4D6d1 average = {method_4 / 100000}')