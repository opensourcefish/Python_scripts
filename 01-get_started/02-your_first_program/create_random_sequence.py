

import random

alphabet = "AGCT"
sequence = ""
for i in range(10):
    index = random.randint(0, 3)
    sequence = sequence + alphabet[index]
    
print (sequence)
