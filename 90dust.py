#!/usr/bin/env python3
import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()


w = int(arg.size)
e = float(arg.entropy)
for defline, seq in mcb185.read_fasta(arg.file):
	print(f'>{defline}')
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
			if arg.lower is not True:
				for b in range(w):
					output[a + b] = 'N'
			elif arg.lower is True:
				for b in range(w):
					if seq[a + b] == 'A':   output[a + b] = 'a'
					elif seq[a + b] == 'C': output[a + b] = 'c'
					elif seq[a + b] == 'G': output[a + b] = 'g'
					elif seq[a + b] == 'T': output[a + b] = 't'
					elif seq[a + b] == 'N': output[a + b] = 'n'
	num = 0
	for a in output:
		if num == 60:
			print()
			num = 0
		print(a, end='')
		num += 1
	print()			