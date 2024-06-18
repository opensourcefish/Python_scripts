input_file = open('list_old.txt', 'r')
output_file = open('list_even_lines.txt','w')

index = 0
for line in input_file:
    index = index + 1
    if index % 2 == 0:
        output_file.write(line)

input_file.close()
output_file.close()
