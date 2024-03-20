import gzip
import sys
import dogma


with gzip.open(sys.argv[1], 'rt') as data:
	seq = []
	genes = []
	is_seq = False
	for line in data:
		if is_seq is True:
			seq.append(''.join(line.split()[1:]))
		if is_seq is False:
			data = line.split()
			if data[0] == 'gene':
				genes.append(data[1])
			elif data[0] == 'ORIGIN':
				is_seq = True
	seq = ''.join(seq)
	output = []
	for a in genes:
		if 'complement' in a:
			start = int(a[11:-1].split('..')[1])
			string = dogma.revcomp(seq[start-4:start+10])
			for b in range(len(string)):
				if b == len(output):
					output.append({'a': 0, 'c': 0, 'g': 0, 't': 0})
				if string[b] != 'N':
					output[b][string[b]] += 1
		else:
			start = int(a.split('..')[0])
			string = seq[start-10:start+4]
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
	for a in range(14):
		print(f'{a+1}\t{output[a]["a"]:<5}\t{output[a]["c"]:<5}\t{output[a]["g"]:<5}\t{output[a]["t"]:<5}')
	print('XX')