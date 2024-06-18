'''

Calculate the differences of two sets


'''

data_a = set([1, 2, 3, 4, 5, 6])
data_b = set([1, 5, 7, 8, 9])

a_not_b = data_a.difference(data_b)
b_not_a = data_b.difference(data_a)

print (a_not_b)
print (b_not_a)


# see also:
a_or_b = data_a.union(data_b)
a_xor_b = data_a.symmetric_difference(data_b)

print (a_or_b)
print (a_xor_b)
