
input_file = open("SwissProtSeq.fasta","r")
ac_list = []

for line in input_file:
    if line[0] == '>':
        fields = line.split('|')
        ac_list.append(fields[1])

print (ac_list)
