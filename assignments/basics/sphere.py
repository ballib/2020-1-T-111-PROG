import math
r_str = input('Input radius: ')
r = float(r_str)
volume = (4/3) * math.pi * r**3
area = 4 * math.pi * r**2

print('Volume:', volume)
print('Area:', area)