'''
Remove duplicates from a list of accession numbers
Using a list (easier to write but slow for big files).
'''

input_file = open('UniprotID.txt')
output_file = open('UniprotID-unique.txt','w')

unique = []
for line in input_file:
    if line not in unique:
        output_file.write(line)
        unique.append(line)

input_file.close()
output_file.close()
