import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

tot = 0
for a in range(trials):
	same = False
	birthdays = []
	for b in range(people):
		birthdays.append(random.randint(1, days))
	birthdays.sort()
	print(birthdays)
	for b in range(people):
		if birthdays[b - 1] == birthdays[b]:
			same = True
	if same == True:
		tot += 1
			

print(f'{tot * 100 / trials:.2f}%')