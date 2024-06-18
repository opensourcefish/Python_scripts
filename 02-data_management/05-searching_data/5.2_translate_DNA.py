
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
}

out_file_1 = open('DNA-translate.fasta','w')
out_file_2 = open('start_stop_codons.txt','w')
# read the RNA sequence into a single string
dna = ''
for line in open('snake_DNA.fasta'):
    if line.startswith('>'):
        AC = line.split(' ')[0].strip()

    if not line.startswith('>'): 
        dna = dna + line.strip()

# translate one frame at a time
for frame in range(3):
    prot = '' 
    out_file_1.write('\n' + AC + ' ' + 'Reading frame' + ' ' + str(frame + 1) + '\n' )
    m = 0
    n = 0
    for i in range(frame, len(dna), 3):
        codon = dna[i:i + 3]
        
        if codon in codon_table:
            if codon_table[codon] == '*':
                prot = prot + '*'
                m = m + 1
            
            elif codon_table[codon] == 'M':
                prot = prot + 'M'
                n = n + 1
                
            else: 
                prot = prot + codon_table[codon]
            
        else:
            # handle too short codons
            prot = prot + '-'

    # format to blocks of 64 columns
    i = 0
    while i < len(prot):
        out_file_1.write(prot[i:i + 64])
        i = i + 64

    out_file_2.write('\n' + AC + ' ' + 'Reading frame' + ' ' + str(frame + 1) + '\n' )
    out_file_2.write('start codon numbers:' + ' ' + str(n) + '\n')
    out_file_2.write('stop codon numbers:' + ' ' + str(m))
