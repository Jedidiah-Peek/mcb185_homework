# 35nchoosek.py by Jedidiah_Peek

def factorial(num):
	output = 1
	for a in range(1, num + 1):
		output = output * a
	return output

def nchoosek(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))


print(int(nchoosek(10, 5)))
print(int(nchoosek(9, 9)))
print(int(nchoosek(3, 2)))
print(int(nchoosek(3, 0)))