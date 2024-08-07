'''
Sort entries in a comma separated file by two columns.
'''

from operator import itemgetter

input_file = open("PDBhaemoglobinReport.csv")
output_file = open("PDBhaemoglobinSorted.csv","w")

table = []
header = input_file.readline()
for line in input_file:
    col = line.split(',')
    col[3] = float(col[3][1:-1])
    col[4] = int(col[4][1:-2])
    table.append(col)

table_sorted = sorted(table, key=itemgetter(3, 4))

output_file.write(header)
for row in table_sorted:
    row = [str(x) for x in row]
    output_file.write("\t".join(row) + '\n')

input_file.close()
output_file.close()
