import random


def probablity(DC):
	nor = 0
	adv = 0
	dis = 0
	for a in range(100000):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 >= DC:              nor += 1
		if d1 >= DC or d2 >= DC:  adv += 1
		if d1 >= DC and d2 >= DC: dis += 1
	print(f'DC\t{nor / 1000:.2f}%\t\t{adv / 1000:.2f}%\t\t{dis / 1000:.2f}%')

print('\tnormal \t\tadvantage \tdisadvantage')
probablity(5)
probablity(10)
probablity(15)