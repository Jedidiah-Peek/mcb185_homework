import gzip
import sys
import dogma


with gzip.open(sys.argv[1], 'rt') as data:
	seq = []
	genes = []
	for line in data:
		if ' gene' in line and '..' in line:
			genes.append(line.split()[1])
		elif '1 ' in line and '/' not in line and '(' not in line:
			for a in line.split()[1:]:
				seq.append(a)
	seq = ''.join(seq)
	output = []
	for a in genes:
		if 'complement' in a:
			points = [int(a[11:-1].split('..')[0]), int(a[11:-1].split('..')[1])]
			string = dogma.revcomp(seq[points[0]:points[1]])
			for b in range(len(string)):
				if b == len(output):
					output.append({'a': 0, 'c': 0, 'g': 0, 't': 0})
				if string[b] != 'N':
					output[b][string[b]] += 1
		else:
			points = [int(a.split('..')[0]), int(a.split('..')[1])]
			string = seq[points[0]:points[1]]
			for b in range(len(string)):
				if b == len(output):
					output.append({'a': 0, 'c': 0, 'g': 0, 't': 0})
				if string[b] != 'N':
					output[b][string[b]] += 1
	print('AC IMTSU001')
	print('XX')
	print('ID ECKOZ')
	print('XX')
	print('DE nt frequency')
	print(f'PO\tA\tC\tG\tT')
	for a in range(len(output)):
		print(f'{a+1}\t{output[a]["a"]}\t{output[a]["c"]}\t{output[a]["g"]}\t{output[a]["t"]}')
	print('XX')