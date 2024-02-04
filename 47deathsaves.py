import random


die = 0
stable = 0
revived = 0

for a in range(100000):
	f = 0
	s = 0
	while f < 3 and s < 3:
		roll = random.randint(1,20)
		if roll == 20:
			revived += 1
			s += 4
		if roll >= 10:
			s += 1
			if s == 3: stable += 1
		if roll == 1:
			f += 1
		if roll < 10:
			f += 1
			if f >= 3: die += 1

print(f'died = {die / 1000:.2f}%, stablized = {stable / 1000:.2f}%, and revived = {revived / 1000:.2f}%')