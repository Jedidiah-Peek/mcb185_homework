import mcb185
import sys
import dogma


def find_cds(nt, size, both):
	l = len(nt)
	out = []
	for frame in range(3):
		last_stop = 0
		for a in range(frame, len(nt)-2, 3):
			if nt[a:a+3] == 'ATG':
				for b in range(a + 3, len(nt)-2, 3):
					if nt[b:b+3] in ('TAA', 'TAG', 'TGA'):
						start = a + 1
						end = b + 3
						if start > last_stop and end - start >= size:
							out.append({'start': start, 'end' : end, 'direction' : '+'})
						last_stop = end
						break
		if both:
			last_stop = 0
			op_nt = dogma.revcomp(nt)
			for a in range(frame, len(nt)-2, 3):
				if nt[a:a+3] == 'ATG':
					for b in range(a + 3, len(nt)-2, 3):
						if nt[b:b+3] in ('TAA', 'TAG', 'TGA'):
							start = a + 1
							end = b + 3
							if start > last_stop and end - start >= size:
								out.append({'start': l - end, 'end' : l - start, 'direction' : '-'})
							last_stop = end
							break
	return out


for defline, seq in mcb185.read_fasta(sys.argv[1]):
	CDS = find_cds(seq, int(sys.argv[2]), True)
	for a, data in enumerate(CDS):
		print(f'E. coli\t74genefinder.py\tCDS\t{data["start"]}\t{data["end"]}\t.\t{data["direction"]}\t0\tpro-{a}')