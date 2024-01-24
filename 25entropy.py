# 25entropy.py by Jedidiah_Peek

import math


def entropy(a, c, g, t):
	if type(a) != int or type(c) != int or type(g) != int or type(t) != int:
		return 'Error: inputs not positive integers'
	
	elif a < 0 or c < 0 or g < 0 or t < 0:
		return 'Error: inputs not positive integers'
	
	else:
		nt = a + c + g + t
		pa = a / nt
		pc = a / nt
		pg = g / nt
		pt = t / nt
		return -(pa * math.log2(pa) + pc * math.log2(pc) + pg * math.log2(pg) + pt * math.log2(pt)) 
		
		
print(entropy(1, 1, 1, 1))
print(entropy(4, 0, 5, 7))
print(entropy('a', 3, 18, 1000))
print(entropy(-1, -11, 111, 1111))
print(entropy(2.5, 8, 30000, 2))