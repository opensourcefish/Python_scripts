import numpy as np
import random

# 1. Generate a DNA file
alphabet = "ATCG"
sequence = ""
output_file = open('codons.txt', 'w')

for i in range(1000):
    index = random.randint(0, 3)
    sequence = sequence + alphabet[index]
    
output_file.write(sequence)
output_file.close()

# 2. Calculating
codons = open ('C:/Users/Bing/Desktop/codons.txt')
lines = codons.read()
length = len(lines)

A_num = lines.count("A")
 
T_num = lines.count("T")

C_num = lines.count("C")

G_num = lines.count("G")

GC_frequency = ( G_num + C_num ) / length * 100 

output = open("codons_results.txt","w")
output.write("A : %4i \n"%(A_num))
output.write("T : %4i \n"%(T_num))
output.write("C : %4i \n"%(C_num))
output.write("G : %4i \n"%(G_num))
output.write("GC (%%): %4.2f \n"%(GC_frequency))

output_file.close()