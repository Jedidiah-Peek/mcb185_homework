import gzip


path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as seq:
	for line in seq:
		if line[0] == '#': continue
		words = line.split()
		if len(words) < 4: continue
		if words[2] != 'CDS': continue
		print(int(words[4])-int(words[3])+1)