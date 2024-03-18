import sys
import mcb185

w = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	C = seq[0:w].count('C')
	G = seq[0:w].count('G')
	print(f'0\t{(C + G) / w:.3f}\t{(G - C) / (G + C):.3f}')
	for a in range(len(seq) - w + 1):
		if seq[a] == 'C':   C -= 1
		elif seq[a] == 'G': G -= 1
		if seq[a + w] == 'C':   C += 1 
		elif seq[a + w] == 'G': G += 1
		print(f'{a + 1}\t{(C + G) / w:.3f}\t{(G - C) / (G + C):.3f}')