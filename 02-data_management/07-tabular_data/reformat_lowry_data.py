'''
Reformat a four-column to a two-column table.
'''

table = [
    ['protein', 'ext1', 'ext2', 'ext3'],
    [0.16, 0.038, 0.044, 0.040],
    [0.33, 0.089, 0.095, 0.091],
    [0.66, 0.184, 0.191, 0.191],
    [1.00, 0.280, 0.292, 0.283],
    [1.32, 0.365, 0.367, 0.365],
    [1.66, 0.441, 0.443, 0.444]
    ]

table = table[1:]

protein, ext1, ext2, ext3 = zip(*table)

extinction = ext1 + ext2 + ext3
protein = protein * 3

table = zip(protein, extinction)

for prot, ext in table:
    print (prot, ext)
    
