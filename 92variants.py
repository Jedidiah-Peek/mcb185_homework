import argparse
import gzip


parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()


with gzip.open(arg.vcf, 'rt') as dif:
	for a in dif:
		info = a.split()
		print(f'{info[0]}\t{info[1]}\t', end='')
		with gzip.open(arg.gff, 'rt') as locate:
			loc = []
			for b in locate:
				places = b.split()
				if places[0] == info[0] and info[1] > places[3] and info[1] < places[4]:
					if places[2] not in loc: loc.append(places[2])
			for word in loc[:-1]:
				print(word, end=',')
			print(loc[-1])