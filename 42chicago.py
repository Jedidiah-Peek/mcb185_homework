import random

total = 0
zeros = 0
for a in range(100000):
	if a % 1000 == 0: print(f'{a / 1000}% done')
	score = 0 
	for b in range(2, 13):
		if random.randint(1, 6) + random.randint(1, 6) == b: score += b
	if score == 0: zeros += 1
	total += score

print(f'average score is {total / 100000}')
print(f'{zeros / 100000}% of games score zero points')