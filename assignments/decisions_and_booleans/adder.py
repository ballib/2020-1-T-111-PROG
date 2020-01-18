a_str = input("Enter value for A: ")
b_str = input("Enter value for B: ")

a_bool = bool(int(a_str))
b_bool = bool(int(b_str))

s_bool = int(a_bool ^ b_bool)
c_bool = int(a_bool and b_bool)

print('S={}, C={}'.format(s_bool, c_bool))