import sys
import math

probs = []
total = 0
h = 0
for a in sys.argv[1:]:
	a = float(a)
	assert(a > 0 and a < 1)
	probs.append(a)
	total += a
	h -= a * math.log2(a)

if not math.isclose(total, 1): sys.exit('Probablities do not total to 1')
print(h)