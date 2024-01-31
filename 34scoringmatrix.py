# 34scoringmatrix.py by Jedidiah_Peek

sequence = 'ACGT'

column1 = ' '
for a in sequence:
	column1 = column1 + ' ' + a
print(column1)
for char in sequence:
	output = char
	for a in sequence:
		if a == char: output = output + '+1'
		else:         output = output + '-1'
	print(output)