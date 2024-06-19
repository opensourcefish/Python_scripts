'''
write the table into a file, then read the file and print the table on the screen
'''
table = [
    ['', 'A', 'G', 'C', 'U'],
    ['A', 1.0, 0.5, 0.0],
    ['G', 0.5, 1.0, 0.0],
    ['C', 0.0, 0.0, 0.5],
    ['U', 0.0, 0.0, 1.0],
    ]

out = ''
for row in table:
    line = [str(cell) for cell in row]
    out = out + '\t'.join(line) + '\n'
open('RNA_matrix.txt', 'w').write(out)

table = []
for line in open('RNA_matrix.txt'):
    table.append(line.strip().split('\t'))
    
print (table)
