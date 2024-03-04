import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

tot = 0
for a in range(trials):
	same = False
	birthdays = []
	for b in range(days):
		birthdays.append(0)
	for b in range(people):
		birthdays[random.randint(0, days - 1)] += 1
	birthdays.sort()
	if birthdays[-1] > 1:
		tot +=1

print(f'{tot * 100 / trials:.2f}%')