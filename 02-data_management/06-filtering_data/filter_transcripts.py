'''
Filter transcripts from NGS.
'''
tracking = open('transcripts.tracking', 'r')
out_file = open('transcripts-filtered.tracking', 'w')

for track in tracking:
    # split tab-separated columns
    columns = track.strip().split('\t')
    wildtype = columns[4:7].count('-')
    treatment = columns[7:10].count('-')
    if wildtype < 2 or treatment < 2:
        out_file.write(track)
	
tracking.close()
out_file.close()
