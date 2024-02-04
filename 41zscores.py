import random

z1 = 1
z2 = 1
z3 = 1
for a in range(2000000):
	value = random.gauss(0, 1)
	if value > 1: z1 -= 0.000001
	if value > 2: z2 -= 0.000001
	if value > 3: z3 -= 0.000001
	
print(z1)
print(z2)
print(z3)