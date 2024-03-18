import sys
import mcb185
import dogma


def thin(seqs, size):
	output = []
	for a in seqs:
		if a.find('*') > size - 2:
			output.append(a[:a.find('*') + 1])
	return output
		

l = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	proteins = 0
	for a in range(3):
		possible = dogma.translate(seq[a:]).split('M')
		pro = thin(possible, l)
		for b in pro:
			print(f'>pro-{proteins}')
			print(f'M{b}')
			proteins += 1
		possible = dogma.translate(dogma.revcomp(seq)[a:]).split('M')
		pro = thin(possible, l)
		for b in pro:
			print(f'>pro-{proteins}')
			print(f'M{b}')
			proteins += 1