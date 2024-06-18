'''
Remove some lines from a text file.

'''

in_file = open('text.txt')
out_file = open('new.txt', 'w')

index = 0
indices_to_remove = [1, 2, 5, 6]
for line in in_file:
    index = index + 1
    if index not in indices_to_remove:
        out_file.write(line)

in_file.close()
out_file.close()
