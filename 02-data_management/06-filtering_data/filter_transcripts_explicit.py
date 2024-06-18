'''
Filter a file with transcripts.
Each transcript must be annotated in 2+ wildtype columns
and 2+ sample columns.

'''

output_file = open('transcripts-filtered.tracking', 'w')

for track in open('transcripts.tracking'):
    columns = track.strip().split('\t')
    wt = 0
    t = 0
    if columns[4] != '-': wt += 1
    if columns[5] != '-': wt += 1
    if columns[6] != '-': wt += 1
    if columns[7] != '-': t += 1
    if columns[8] != '-': t += 1
    if columns[9] != '-': t += 1
    if wt > 1 or t > 1:
        output_file.write(track)

output_file.close()	
