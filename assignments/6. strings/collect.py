a_str = input("Input a string: ")
number_str = ''
for i, c in enumerate(a_str):
    if (c.isdigit() or c == '.') and i < len(a_str) - 1:
        number_str += c
    else:
        if len(number_str) > 0:
           print(number_str)
        number_str = ''