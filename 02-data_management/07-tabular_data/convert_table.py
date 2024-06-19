'''
Convert a table from a nested list to a nested dictionary and back.
'''

table = [
    ['protein', 'ext'],
    [0.16, 0.038],
    [0.33, 0.089],
    [0.66, 0.184],
    [1.00, 0.280],
    [1.32, 0.365],
    [1.66, 0.441]
    ]

# convert nested list to nested dict
nested_dict = {}
for row in table:
    entry = {'protein': row[0], 'ext': row[1]}
    nested_dict[row[0]] = entry
print (nested_dict)

# convert nested dict back to nested list
nested_list = []
for entry in table:
    nested_list.append([entry['protein'], entry['ext']])
print (nested_list)
