# 24accuracy.py by Jedidiah_Peek

def accuracy(tp, fp, tn, fn):
	if type(tp) != int or type(fp) != int or type(tn) != int or type(fn) != int:
		return 'Error: inputs not positive integers'
	
	elif tp < 0 or fp < 0 or tn < 0 or fn < 0:
		return 'Error: inputs not positive integers'
	
	else:
		return (tp + tn) / (tp + fp + tn + fn), tp / (tp + 0.5 * (fp + fn))
		

print(accuracy(1, 1, 1, 1))
print(accuracy(2, 5, 1, 'a'))
print(accuracy(1, 1, -18, 1))
print(accuracy(1, 0, 0, 20))
print(accuracy(30, 8.5, 3, 27))