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
	
	
gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
def translate(seq):
	pro = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon in gcode: aa = gcode[codon]
		else:              aa = 'X'
		pro.append(aa)
	return ''.join(pro)
	

def print_pwm(name, ID, de, pwm):
	print('AC', name)
	print('XX')
	print('ID', ID)
	print('XX')
	print('DE', de)
	print('PO\tA\tC\tG\tT')
	for i, count in enumerate(pwm):
		a_count = count['A']
		c_count = count['C']
		g_count = count['G']
		t_count = count['T']
		print(f'{i+1:<8}{a_count:<8}{c_count:<8}{g_count:<8}{t_count:<8}')
	print('XX')
	print('//')
	
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)


def temp_melt(seq):
	nt_count = len(seq)
	a = seq.count('A')
	c = seq.count('C')
	g = seq.count('G')
	t = seq.count('T')
	if nt_count <= 13:
		return (a + t) * 2 + (g + c) * 4
		
	else:
		return 64.9 + 41 * (g + c - 16.4) /nt_count
		

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
		