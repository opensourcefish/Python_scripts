'''
Sort a table by one column and write it to a file.
'''

from operator import itemgetter

# read table to a nested list of floats
table = []
for line in open("random_distribution.tsv"):
    columns = line.split()
    columns = [float(x) for x in columns]
    table.append(columns)

# sort the table by second column
column = 1
table_sorted = sorted(table, key = itemgetter(column))

# format table as strings
for row in table_sorted:
    row = [str(x) for x in row]
    print ("\t".join(row))
