import argparse
import gzip


parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()


with gzip.open(arg.vcf, 'rt') as dif:
	changes = []
	for a in dif:
		info = a.split()
		changes.append({'chr' : info[0], 'place' : info[1], 'type' : []})
		
with gzip.open(arg.gff, 'rt') as locate:
	for a in locate:
		data = a.split()
		for point in changes:
			if point['chr'] == data[0] and int(point['place']) > int(data[3]) and int(point['place']) < int(data[4]):
				if data[2] not in point['type']: point['type'].append(data[2])
				
for a in changes:
	if len(a['type']) > 0: print(f'{a["chr"]}\t{a["place"]}\t{",".join(a["type"])}')