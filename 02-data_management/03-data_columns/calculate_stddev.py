
import math

data = [3.53, 3.47, 3.51, 3.72, 3.43]
average = sum(data) / len(data)

total = 0.0
for value in data:
    total += (value - average) ** 2
stddev = math.sqrt(total / len(data))

print (stddev)
