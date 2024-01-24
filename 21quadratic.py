# 21quadratic.py by Jedidiah_Peek

import sys
import math

def quad(a, b, c):
	if a == 0:
		return 'Not quadradic equation'
		
	elif b**2 < 4*a*c:
		return 'No real solutions'
		
	elif b**2 == 4*a*c:
		return -b / (2*a)
		
	else:
		return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
		
		
print(quad(2, 2, 3))
print(quad(0, 2, 3))
print(quad(3, -7, 3))
print(quad(2, 4, 2))