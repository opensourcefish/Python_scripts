'''
Sort a table by one column and write it to a file.
'''

from operator import itemgetter

input_file = open("lowry_data.txt")
output_file = open("sorted_lowry_data.txt","w")

# read table to a nested list of floats
table = []
header = input_file.readline()
output_file.write(header)

for line in input_file:
    columns = line.split()
    columns = [float(x) for x in columns]
    table.append(columns)

# sort the table by second column
column = 1
table_sorted = sorted(table, key = itemgetter(column))

# format table as strings
for row in table_sorted[:3]:
    row = [str(x) for x in row]
    output_file.write("\t".join(row) + '\n')


input_file.close()
output_file.close()