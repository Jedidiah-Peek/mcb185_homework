import gzip
import sys
import dogma
import mcb185


with gzip.open(sys.argv[1], 'rt') as data:
	genesf = {}
	genesr = {}
	for line in data:
		stuff = line.split()
		if stuff[1] =='RNASeq_splice':
			if stuff[6] == '+':
				if stuff[0] not in genesf: genesf[stuff[0]] = []
				points = [int(stuff[3]), int(stuff[4])]
				genesf[stuff[0]].append(points)
			elif stuff[6] == '-':
				if stuff[0] not in genesr: genesr[stuff[0]] = []
				points = [int(stuff[3]), int(stuff[4])]
				genesr[stuff[0]].append(points)
	acc = []
	don = []
	for defline, seq in mcb185.read_fasta(sys.argv[2]):
		sec = defline.split()[0]
		if sec in genesf:
			for a in genesf[sec]:
				string = seq[a[0]:a[1]]
				for b in range(7):
					if b == len(don):
						don.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
					if string[b] != 'N':
						don[b][string[b]] += 1
				for b in range(6):
					if b == len(acc):
						acc.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
					if string[-6+b] != 'N':
						acc[b][string[b - 6]] += 1
		if sec in genesf:
			for a in genesr[sec]:
				string = dogma.revcomp(seq[a[0]:a[1]])
				for b in range(7):
					if b == len(don):
						don.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
					if string[b] != 'N':
						don[b][string[b]] += 1
				for b in range(6):
					if b == len(acc):
						acc.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
					if string[-6+b] != 'N':
						acc[b][string[b - 6]] += 1
	print('AC OUTPUT1')
	print('XX')
	print('ID ACC')
	print('XX')
	print('DE splice acceptor')
	print(f'PO\tA\tC\tG\tT')
	for a in range(len(acc)):
		print(f'{a+1}\t{acc[a]["A"]}\t{acc[a]["C"]}\t{acc[a]["G"]}\t{acc[a]["T"]}')
	print('XX')
	print('//')
	print('AC OUTPUT2')
	print('XX')
	print('ID DON')
	print('XX')
	print('DE splice donnor')
	print(f'PO\tA\tC\tG\tT')
	for a in range(len(don)):
		print(f'{a+1}\t{don[a]["A"]}\t{don[a]["C"]}\t{don[a]["G"]}\t{don[a]["T"]}')
	print('XX')
	print('//')