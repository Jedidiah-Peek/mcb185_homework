import sys
import mcb185
import dogma


def hydropathy(seqs):
	hydro = 0
	for aa in seqs:
		if aa == 'A':   hydro += 1.80
		elif aa == 'C': hydro += 2.50
		elif aa == 'D': hydro += -3.50
		elif aa == 'E': hydro += -3.50
		elif aa == 'F': hydro += 2.80
		elif aa == 'G': hydro += -0.40
		elif aa == 'H': hydro += -3.20
		elif aa == 'I': hydro += 4.50
		elif aa == 'K': hydro += -3.90
		elif aa == 'L': hydro += 3.80
		elif aa == 'M': hydro += 1.90
		elif aa == 'N': hydro += -3.50
		elif aa == 'P': hydro += -1.60
		elif aa == 'Q': hydro += -3.50
		elif aa == 'R': hydro += -4.50
		elif aa == 'S': hydro += -0.80
		elif aa == 'T': hydro += -0.70
		elif aa == 'V': hydro += 4.20
		elif aa == 'W': hydro += -0.90
		elif aa == 'Y': hydro += -1.30
	return hydro / len(seqs)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	signal = False
	trans = False
	if len(seq) > 30:
		for a in range(0, 23):
			if seq[a:a + 8].find('P') == -1 and hydropathy(seq[a:a + 8]) >= 2.5:
				signal = True
	if signal is True:
		for a in range(30, len(seq) - 10):
			if seq[a:a + 11].find('P') == -1 and hydropathy(seq[a:a + 11]) >= 2:
				trans = True
	if trans is True:
		print(f'>{defline}')
	