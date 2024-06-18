fasta_file = open('SwissProt.fasta','r')

seq = ''
for line in fasta_file:
    if line[0] == '>' and seq == '':
        # process the first line of the input file
        header = line
        AC = header.split('|')[1].strip()
        
    elif line [0] != '>':
        # join the lines with sequence
        seq = seq + line

    elif line[0] == '>' and seq != '':
        # in subsequent lines starting with '>',
        # write the previous header and sequence
        # to the output file. Then re-initialize
        # the header and seq variables for the next record
        out_file = open(AC,'w')
        out_file.write(header + seq)
        out_file.close() 
        seq = ''
        header = line
        AC = header.split('|')[1].strip()

