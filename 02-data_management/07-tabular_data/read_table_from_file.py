'''
Read tabular data from a tab-separated text file
'''

table = []
for line in open('lowry_data.txt'):
    table.append(line.strip().split('\t'))
    
print (table)
