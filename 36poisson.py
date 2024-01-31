# 36poisson.py by Jedidiah_Peek

import math

def factorial(num):
	output = 1
	for a in range(1, num + 1):
		output = output * a
	return output

def poisson(k, n):
	return ((n ** k) * (math.e ** -n)) / (factorial(k))


print(poisson(1, 0.5))
print(poisson(4, 0.5))
print(poisson(10, 1))
print(poisson(2, 0))