import mcb185
import sys
import dogma


def cds_f(nt, size, num):
	for frame in range(3):
		last_stop = 0
		for a in range(frame, len(nt)-2, 3):
			if nt[a:a+3] == 'ATG':
				for b in range(a + 3, len(nt)-2, 3):
					if nt[b:b+3] in ('TAA', 'TAG', 'TGA'):
						start = a + 1
						end = b + 3
						if start > last_stop and end - start >= size:
							print(f'E. coli\t74genefinder.py\tCDS\t{start}\t{end}\t.\t+\t0\tpro-{num}')
							num += 1
						last_stop = end
						break
	return num

def cds_r(nt, size, num):
	l = len(nt)
	for frame in range(3):
		last_stop = 0
		for a in range(frame, len(nt)-2, 3):
			if nt[a:a+3] == 'ATG':
				for b in range(a + 3, len(nt)-2, 3):
					if nt[b:b+3] in ('TAA', 'TAG', 'TGA'):
						start = a + 1
						end = b + 3
						if start > last_stop and end - start >= size:
							print(f'E. coli\t74genefinder.py\tCDS\t{l - end}\t{l - start}\t.\t-\t0\tpro-{num}')
							num += 1
						last_stop = end
						break
						

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	CDS = 0
	CDS = cds_f(seq, int(sys.argv[2]), CDS)
	CDS = cds_r(dogma.revcomp(seq), int(sys.argv[2]), CDS)