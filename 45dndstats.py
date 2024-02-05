import random


method_1 = 0
method_2 = 0
method_3 = 0
method_4 = 0
d2 = random.randint(1, 6)

for a in range(100000):
	lowest = d2
	for b in range(3):
		method_2 += random.randint(2, 6)
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		method_1 += d1
		if d1 > d2: method_3 += d1
		else:       method_3 += d2
		if d1 >= lowest:
			method_4 += d1
		else:
			method_4 += lowest
			lowest = d1


print(f'3D6 average = {method_1 / 100000}')
print(f'3D6r1 average = {method_2 / 100000}')
print(f'3D6x2 average = {method_3 / 100000}')
print(f'4D6d1 average = {method_4 / 100000}')