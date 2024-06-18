

data = [16.38, 139.90, 441.46, 29.03, 40.93, 202.07, 142.30, 346.00, 300.00]

out = []
for value in data:
    out.append(str(value) + '\n')
open('results.txt', 'w').writelines(out)
