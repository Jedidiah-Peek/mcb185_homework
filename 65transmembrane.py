import sys
import mcb185
import dogma


def test(nt, size, cutoff):
	for a in range(0, len(nt) - size + 1):
		if nt[a:a + size].find('P') == -1 and dogma.hydropathy(seq[a:a + size]) >= cutoff:
			return True
	return False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if test(seq[:30], 8, 2.5) is True and test(seq[30:], 11, 2) is True:
		print(f'>{defline}')
	