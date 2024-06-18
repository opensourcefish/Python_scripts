codon_file = open ('snake_DNA.fasta')
out_file = open('snake_DNA_frequency.txt','w')

seq = ''
for line in codon_file:

    if line[0] == '>' and seq == '':
        # process the first line of the input file
        header = line.split(' ')[0] + "\n"
        
    elif line[0] != '>' and line.strip != '':
        # join the lines with sequence
        seq = line
        length = len(seq)

        A_num = seq.count("A")
        A_frequency = A_num / length * 100

        T_num = seq.count("T")
        T_frequency = T_num / length * 100

        C_num = seq.count("C")
        C_frequency = C_num / length * 100

        G_num = seq.count("G")
        G_frequency = G_num / length * 100
         

    elif line[0] == '>' and seq != '':
        # in subsequent lines starting with '>',
        # write the previous header and sequence
        # to the output file. Then re-initialize
        # the header and seq variables for the next record
        
        out_file.write(header)
        out_file.write("A : %2.2f \n"%(A_frequency))
        out_file.write("T : %2.2f \n"%(T_frequency))
        out_file.write("C : %2.2f \n"%(C_frequency))
        out_file.write("G : %2.2f \n"%(G_frequency))
        
        seq = ''
        header = line.split(' ')[0] + "\n"