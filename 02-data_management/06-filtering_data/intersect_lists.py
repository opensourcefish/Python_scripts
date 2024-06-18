'''
Calculate the intersection of two lists
'''

data_a = [1, 2, 3, 4, 5, 6]
data_b = [1, 5, 7, 8, 9]

a_and_b = []

for num in data_a:
    if num in data_b:
        a_and_b.append(num)

print (a_and_b)
