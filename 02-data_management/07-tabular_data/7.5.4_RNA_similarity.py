'''
calculate the similarity between two sequences
'''
seq1 = 'AGCAUCUA'
seq2 = 'ACCGUUCU'
n = 0
m = 0
for base1, base2 in zip(seq1, seq2):
    n = n + 1
    if base1 == base2:
        m = m + 1
similarity = m/n
print (similarity)
        
