import random

num_seq = 5
for a in range(1, num_seq + 1):
	print(f'>seq-{a}')
	for b in range(random.randint(50, 75)):
		print(random.choice('ACGT'), end='')
	print()