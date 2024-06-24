'''
Sort a table by seven columns in one operation.
'''

from operator import itemgetter

# read table
in_file = open("random_distribution.tsv")
table = []
for line in in_file:
    columns = line.split()
    columns = [float(x) for x in columns]
    table.append(columns)

table_sorted = sorted(table, key=itemgetter(0, 1, 2, 3, 4, 5, 6))
print (table_sorted)
    
