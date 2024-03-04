import random


die = 0
stable = 0
revived = 0

for a in range(100000):
	fail = 0
	success = 0
	while fail < 3 and success < 3:
		roll = random.randint(1,20)
		if roll == 20:                    # checks for revive and prevents counting revive & stable
			revived += 1
			success += 4
		if roll >= 10:                    # adds success and checks for stable
			success += 1
			if success == 3: stable += 1
		if roll == 1:                     # adds second fail for nat 1
			fail += 1
		if roll < 10:                     # checks for fail and dying
			fail += 1
			if fail >= 3: die += 1

print(f'died = {die / 1000:.2f}%, stabilized = {stable / 1000:.2f}%, and revived = {revived / 1000:.2f}%')