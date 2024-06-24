'''
Convert a dictionary to a sorted list.
'''

data = {1: 'a', 2: 'b', 4: 'd', 3: 'c',
        5: 't', 6: 'm', 36: 'z'}

# create a list of keys and go through them one by one
keys = list(data)
keys.sort()
for key in keys:
    print (key, data[key])


# sort keys using the sorted() built-in function
for key in sorted(data):
    print (key, data[key])
