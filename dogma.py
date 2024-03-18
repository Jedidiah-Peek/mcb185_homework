def transcribe(dna):
	return dna.replace('T', 'U')
	

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A':   rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)
	
	
def translate(dna):
	aas = []
	for a in range(0, len(dna), 3):
		nt = dna[a:a+3]
		if nt == 'ATG':	
			aas.append('M')
		elif nt == 'CGC' or nt == 'CGT' or nt == 'CGA' or nt == 'CGG' or nt == 'AGA' or nt == 'AGG':
			aas.append('R')
		elif nt == 'CAT' or nt == 'CAC':
			aas.append('H')
		elif nt == 'AAA' or nt == 'AAG':
			aas.append('K')
		elif nt == 'GAT' or nt == 'GAC':
			aas.append('D')
		elif nt == 'GAA' or nt == 'GAG':
			aas.append('E')
		elif nt == 'TCC' or nt == 'TCT' or nt == 'TCA' or nt == 'TCG' or nt == 'AGT' or nt == 'AGC':
			aas.append('S')
		elif nt == 'ACC' or nt == 'ACT' or nt == 'ACA' or nt == 'ACG':
			aas.append('T')
		elif nt == 'AAT' or nt == 'AAC':
			aas.append('N')
		elif nt == 'CAA' or nt == 'CAG':
			aas.append('Q')
		elif nt == 'TGT' or nt == 'TGC':
			aas.append('C')
		elif nt == 'GGG' or nt == 'GGT' or nt == 'GGA' or nt == 'GGC':
			aas.append('G')
		elif nt == 'CCC' or nt == 'CCT' or nt == 'CCA' or nt == 'CCG':
			aas.append('P')
		elif nt == 'GCC' or nt == 'GCG' or nt == 'GCA' or nt == 'GCT':
			aas.append('A')
		elif nt == 'GTT' or nt == 'GTG' or nt == 'GTA' or nt == 'GTC':
			aas.append('V')
		elif nt == 'ATT' or nt == 'ATC' or nt == 'ATA':
			aas.append('I')
		elif nt == 'TTA' or nt == 'TTG' or nt == 'CTT' or nt == 'CTC' or nt == 'CTG' or nt == 'CTA':
			aas.append('L')
		elif nt == 'TTT' or nt == 'TTC':
			aas.append('F')
		elif nt == 'TAT' or nt == 'TAC':
			aas.append('Y')
		elif nt == 'TGG':
			aas.append('W')
		elif nt == 'TAA' or nt == 'TAG' or nt == 'TGA':
			aas.append('*')
		else:
			aas.append('X')
	return ''.join(aas)
	
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)