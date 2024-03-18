import sys
import mcb185
import math

w = int(sys.argv[2])
e = float(sys.argv[3])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)
	output = list(seq)
	for a in range(len(seq) - w + 1):
		s = seq[a:w + a]
		ent = 0
		if s.count('A') > 0:
			ent += s.count('A') / w * math.log2(s.count('A') / w)
		if s.count('C') > 0:
			ent += s.count('C') / w * math.log2(s.count('C') / w)
		if s.count('G') > 0:
			ent += s.count('G') / w * math.log2(s.count('G') / w)
		if s.count('T') > 0:
			ent += s.count('T') / w * math.log2(s.count('T') / w)
		ent *= -1
		if ent < e:
			for b in range(w):
				output[a + b] = 'N'
	print(''.join(output))