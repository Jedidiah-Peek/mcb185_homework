import sys
import mcb185
import dogma
		

def prot(aa, num):
	while 'M' in aa and '*' in aa:
			aa = aa[aa.find('M'):]
			if aa.find('*') >= l - 1:
				print(f'>pro-{num}')
				print(aa[:aa.find('*') + 1])
				num += 1
				aa = aa[1:]
			else:
				aa = aa[aa.find('*') + 1:]
	return num


l = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	proteins = 0
	for a in range(3):
		proteins = prot(dogma.translate(seq[a:]), proteins)
		proteins = prot(dogma.translate(dogma.revcomp(seq)[a:]), proteins)