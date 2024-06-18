fasta_file = open('SwissProt.fasta','r')
out_file = open('SwissProt.filtered.fasta','w')

seq = ''

for line in fasta_file:
    if line[0] == '>' and seq == '':
        # process the first line of the input file
        header = line
    elif line [0] != '>':
        # join the lines with sequence
        seq = seq + line
    elif line[0] == '>' and seq != '':
        # in subsequent lines starting with '>',
        # write the previous header and sequence
        # to the output file. Then re-initialize
        # the header and seq variables for the next record
        if seq[0] == 'M' and seq.count('W') > 1:
            out_file.write(header + seq)
        seq = ''
        header = line

