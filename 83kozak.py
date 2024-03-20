import gzip
import sys
import dogma
import mcb185


def get_seq(file):
	genome = []
	with gzip.open(file, 'rt') as data:
		for line in data:
			if 'ORIGIN' in line:
				break
		for line in data:
			words = line.upper().split()
			for word in words[1:]:
				genome.append(word)
	return ''.join(genome)
	
			
genome_seq = get_seq(sys.argv[1])

kozaks = []
for i in range(14):
	kozaks.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

with gzip.open(sys.argv[1], 'rt') as lines:
	for line in lines:
		data = line.split()
		if data[0] != 'CDS' or 'join' in data[1]:
			continue

		if 'complement' in data[1]:
			place = data[1][data[1].index('('):data[1].index(')')]
			idx = int(place.split('..')[1])
			seq = mcb185.anti_seq(genome_seq[idx-5:idx+9])
		else:
			place = data[1]
			idx = int(place.split('..')[0])
			seq = genome_seq[idx-10:idx+4]

		for i, nt in enumerate(seq):
			kozaks[i][nt] += 1

dogma.print_pwm('IMTSU001', 'ECKOZ', 'E. coli Kozak sequence', kozaks)