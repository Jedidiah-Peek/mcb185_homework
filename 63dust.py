import sys
import mcb185
import math

w = int(sys.argv[2])
entropy_min = float(sys.argv[3])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(f'>{defline}')
	output = list(seq)
	for a in range(len(seq) - w + 1):
		s = seq[a:w + a]
		ent = 0
		if s.count('A') > 0:
			ent -= s.count('A') / w * math.log2(s.count('A') / w)
		if s.count('C') > 0:
			ent -= s.count('C') / w * math.log2(s.count('C') / w)
		if s.count('G') > 0:
			ent -= s.count('G') / w * math.log2(s.count('G') / w)
		if s.count('T') > 0:
			ent -= s.count('T') / w * math.log2(s.count('T') / w)
		if ent < entropy_min:
			for b in range(w):
				output[a + b] = 'N'
	num = 0
	for a in output:
		if num == 60:
			print()
			num = 0
		print(a, end='')
		num += 1
	print()			