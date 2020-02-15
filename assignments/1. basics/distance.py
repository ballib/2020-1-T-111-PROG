import math

x1_str = input("Input x1: ")
y1_str = input("Input y1: ")
z1_str = input("Input z1: ")
x2_str = input("Input x2: ")
y2_str = input("Input y2: ")
z2_str = input("Input z2: ")

x1_int = int(x1_str)
y1_int = int(y1_str)
z1_int = int(z1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)
z2_int = int(z2_str)

d = math.sqrt((x1_int - x2_int)**2 + (y1_int - y2_int)**2 + (z1_int - z2_int)**2)
print("d =",d)