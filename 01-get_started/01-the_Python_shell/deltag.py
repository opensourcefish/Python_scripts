

ATP = 3.5
ADP = 1.8
Pi = 5.0
R = 0.00831
T = 298
deltaG0 = -30.5

import math
print (deltaG0 + R * T * math.log(ADP * Pi / ATP))
