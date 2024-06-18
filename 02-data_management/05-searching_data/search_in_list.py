'''
Search for non-header lines in a FASTA file.
'''

rna = ''
for line in open('A06662-RNA.fasta'):
    if not line.startswith('>'): 
        rna = rna + line.strip()
