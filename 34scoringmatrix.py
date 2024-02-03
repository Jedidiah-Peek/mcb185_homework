# 34scoringmatrix.py by Jedidiah_Peek

sequence = 'ACGT'

print('   ', end='')
for a in sequence:
	print(a, end='  ')
for char in sequence:
	print()
	print(char, end=' ')
	for a in sequence:
		if a == char: print('+1', end=' ')
		else:         print('-1', end=' ')