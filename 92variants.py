import argparse
import gzip


parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()


with gzip.open(arg.vcf, 'rt') as dif:
	points = []
	for a in dif:
		info = a.split()
		points.append([info[0], info[1]])
		
for a in points:
	loc = []
	with gzip.open(arg.gff, 'rt') as locate:
		for b in locate:
			places = b.split()
			if places[0] == a[0] and int(a[1]) > int(places[3]) and int(a[1]) < int(places[4]):
				if places[2] not in loc:
					loc.append(places[2])
		if len(loc) > 0: print(f'{a[0]}\t{a[1]}\t{",".join(loc)}')