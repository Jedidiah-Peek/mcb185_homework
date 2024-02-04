import random
import math

inside = 0
runs = 0
while True:
	runs += 1
	if math.sqrt(random.random() ** 2 + random.random() ** 2) < 1: inside += 1
	print(f'pi = {4 * inside / runs}')