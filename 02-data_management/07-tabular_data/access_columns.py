'''
Access columns in a nested list.
'''

data = [
    [ 0,  1,  2,  3],
    [10, 11, 12, 13],
    [20, 21, 22, 23]
    ]

columns = zip(*data)
print (columns)