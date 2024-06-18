'''

Calculate the differences of two lists

'''

data_a = [1, 2, 3, 4, 5, 6]
data_b = [1, 5, 7, 8, 9]

a_not_b = []
b_not_a = []

for num in data_a:
    if num not in data_b:
        a_not_b.append(num)
        
for num in data_b:
    if num not in data_a:
        b_not_a.append(num)

print (a_not_b)
print (b_not_a)
