# 37nilakantha.py by Jedidiah_Peek

pi = 3
num = 3
sign = 1
for a in range(100):
	pi = pi + sign * (4 / ((num - 1) * num * (num + 1)))
	num = num + 2
	sign = -sign
print(pi)