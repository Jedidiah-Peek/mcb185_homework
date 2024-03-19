import itertools
import mcb185
import sys
import dogma


missing = False
k = 1
while missing is False:
	kcount = {}
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		for a in range(len(seq) - k + 1):
			kmer = seq[a:a+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
		rev = dogma.revcomp(seq)
		for a in range(len(rev) - k + 1):
			kmer = rev[a:a+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
	for nts in itertools.product('ACGT', repeat=k):
		kmer = ''.join(nts)
		if kmer not in kcount:
			print(kmer)
			missing = True
	k += 1