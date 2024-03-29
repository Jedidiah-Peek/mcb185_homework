import argparse
import mcb185
import dogma


parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100,
	help='minimum protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', help='also examine the anti-parallel strand')
arg = parser.parse_args()

def print_rows(seq):
	for a in range(0, len(seq), 60):
		print(seq[a:a+60])


for defline, seq in mcb185.read_fasta(arg.file):
	trans = dogma.translate(seq[seq.find('ATG'):])
	if '*' in trans and trans.find('*') + 1 >= arg.min:
		print(f'>{defline}')
		print_rows(trans[:trans.find('*')])
	if arg.anti:
		op = dogma.revcomp(seq)
		if 'ATG' in op:
			optrans = dogma.translate(op[op.find('ATG'):])
			if '*' in optrans and optrans.find('*') + 1 >= arg.min:
				print(f'>{defline} anti')
				print_rows(optrans[:optrans.find('*')])