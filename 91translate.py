import argparse
import mcb185
import dogma


parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100,
	help='minimum protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', help='also examine the anti-parallel strand')
arg = parser.parse_args()


for defline, seq in mcb185.read_fasta(arg.file):
	trans = dogma.translate(seq)
	if len(trans) >= arg.min:
		print(defline)
		print(trans)
	if arg.anti is True:
		optrans = dogma.translate(dogma.revcomp(seq))
		if len(optrans) >= arg.min:
			print(defline, 'anti')
			print(trans)