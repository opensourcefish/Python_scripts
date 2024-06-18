'''
Write all headers from a FASTA file to a separate file.
'''

fasta_file = open('SwissProt.fasta','r')
out_file = open('SwissProt.header','w')

for line in fasta_file:
    if line[0:1] == '>':
        out_file.write(line)
out_file.close()
