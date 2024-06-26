import numpy as np

data = []

for line in open ('C:/Users/Bing/Desktop/neuron_data.txt'):
    length = float(line.strip())
    data.append(length)

n_items = len(data)
total = sum(data)
ave = np.mean(data)
sd = np.std(data)
shortest = min(data)
longest = max(data)

data.sort()

output = open("results.txt","w")
output.write("number of dendritic lengths : %4i \n"%(n_items))
output.write("total dendritic length      : %6.1f \n"%(total))
output.write("average dendritic length    : %6.1f \n"%(ave))
output.write("standard deviation length   : %6.1f \n"%(sd))
output.write("shortest dendritic length   : %7.2f \n"%(shortest))
output.write("longest dendritic length    : %7.2f \n"%(longest))
output.write("%37.2f\n%37.2f"%(data [-2], data [-3]))
output.close()