import mcb185
import sys
import dogma


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	CDS = 0
	l = len(seq)
	aa = dogma.translate(seq)
	for a in range(len(aa)):
		if aa[a] == 'M':
			rest = aa[a:]
			b = rest.find('*')
			if b != -1 and b >= 100:
				print(f'E. coli\t74genefinder.py\tCDS\t{3*a}\t{3*(a+b+1)}\t.\t+\t0\tpro-{CDS}')
				CDS += 1
	aa = dogma.translate(seq[1:])
	for a in range(len(aa)):
		if aa[a] == 'M':
			rest = aa[a:]
			b = rest.find('*')
			if b != -1 and b >= 100:
				print(f'E. coli\t74genefinder.py\tCDS\t{3*a+1}\t{3*(a+b+1)+1}\t.\t+\t1\tpro-{CDS}')
				CDS += 1
	aa = dogma.translate(seq[2:])
	for a in range(len(aa)):
		if aa[a] == 'M':
			rest = aa[a:]
			b = rest.find('*')
			if b != -1 and b >= 100:
				print(f'E. coli\t74genefinder.py\tCDS\t{3*a}\t{3*(a+b+1)+1}\t.\t+\t2\tpro-{CDS}')
				CDS += 1
	aa = dogma.translate(dogma.revcomp(seq))
	for a in range(len(aa)):
		if aa[a] == 'M':
			rest = aa[a:]
			b = rest.find('*')
			if b != -1 and b >= 100:
				print(f'E. coli\t74genefinder.py\tCDS\t{l-3*a}\t{l-3*(a+b+1)}\t.\t-\t0\tpro-{CDS}')
				CDS += 1
	aa = dogma.translate(dogma.revcomp(seq)[1:])
	for a in range(len(aa)):
		if aa[a] == 'M':
			rest = aa[a:]
			b = rest.find('*')
			if b != -1 and b >= 100:
				print(f'E. coli\t74genefinder.py\tCDS\t{l-3*a-1}\t{l-3*(a+b+1)-1}\t.\t-\t1\tpro-{CDS}')
				CDS += 1
	aa = dogma.translate(dogma.revcomp(seq)[2:])
	for a in range(len(aa)):
		if aa[a] == 'M':
			rest = aa[a:]
			b = rest.find('*')
			if b != -1 and b >= 100:
				print(f'E. coli\t74genefinder.py\tCDS\t{l-3*a}\t{l-3*(a+b+1)}\t.\t-\t2\tpro-{CDS}')
				CDS += 1
	