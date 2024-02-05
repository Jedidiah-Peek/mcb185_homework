import gzip
import sys
import math


path = sys.argv[1]
feature = sys.argv[2]

with gzip.open(path, 'rt') as data:
	lengths = []
	for line in data:
		words = line.split()
		if words[2] != feature: continue
		lengths.append(int(words[4]) - int(words[3]) + 1)

lengths.sort()
num = len(lengths)
low = lengths[0]
high = lengths[-1]
mean = 0
for a in lengths:
	mean += (a / num)
mean = int(mean)
sd = 0
for a in lengths:
	sd += ((mean - a) ** 2 / num)
sd = int(math.sqrt(sd))
if num // 2 == 0: med = lengths[(num / 2 - 1)]
else:             med = int((lengths[int(num / 2 + 0.5)] + lengths[int(num / 2 - 0.5)]) / 2)

print(f'|{feature}|{num}|{low}|{high}|{mean}|{sd}|{med}|')