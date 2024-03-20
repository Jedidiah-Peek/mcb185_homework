import gzip
import sys
import dogma
import mcb185


with gzip.open(sys.argv[1], 'rt') as data:
	genes_f = []
	genes_r = []
	for line in data:
		stuff = line.split()
		if stuff[1] =='RNASeq_splice':
			if stuff[6] == '+':
				genes_f.append([stuff[0], int(stuff[3]) - 1, int(stuff[4]) - 1])
			elif stuff[6] == '-':
				genes_r.append([stuff[0], int(stuff[3]) - 1, int(stuff[4]) - 1])

chromosomes = {}
for defline, seq in mcb185.read_fasta(sys.argv[2]):
	chromosomes[defline.split()[0]] = seq

don = []	
for a in range(6):
	don.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
acc = []
for a in range(7):
	acc.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
	
	
for a in genes_f:
	intron = chromosomes[a[0]][a[1]:a[2]+1]
	don_seq = intron[:6]
	for num, nt in enumerate(don_seq):
		don[num][nt] += 1 
	acc_seq = intron[-7:]
	for num, nt in enumerate(acc_seq):
		acc[num][nt] += 1 

for a in genes_r:
	intron = dogma.revcomp(chromosomes[a[0]][a[1]:a[2]+1])
	don_seq = intron[0:6]
	for num, nt in enumerate(don_seq):
		don[num][nt] += 1 
	acc_seq = intron[-7:]
	for num, nt in enumerate(acc_seq):
		acc[num][nt] += 1 
		
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