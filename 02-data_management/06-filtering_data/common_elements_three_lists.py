'''

Find numbers common to three lists.


'''
from functools import reduce
 
a = set((1, 2, 3, 4, 5))
b = set((2, 4, 6, 7, 1))
c = set((1, 4, 5, 9))

triple_set = [a, b, c]
common = reduce (set.intersection, triple_set)
print (common)
