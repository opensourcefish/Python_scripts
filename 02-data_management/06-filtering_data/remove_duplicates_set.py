'''

Remove duplicates from a file with accession numbers
Using a set (faster but distorts order)
'''

input_file = open('UniprotID.txt')
output_file = open('UniprotID-unique.txt','w')

unique = set(input_file)
for line in input_file:
    unique.add(line)

for line in unique:
    output_file.write(line)

