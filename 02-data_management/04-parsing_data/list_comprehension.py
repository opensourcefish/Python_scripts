
squares = [x**2 for x in range(5)]
print (squares)

bases = ['A', 'C', 'T', 'G']
print (bases)

seq = 'GGACXCAGXXGATT'
print (seq)

seqlist = [base for base in seq if base in bases]
print (seqlist)
