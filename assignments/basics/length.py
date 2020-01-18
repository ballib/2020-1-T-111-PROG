cm_str = input("Input cm: ")
cm_float = float(cm_str)

inches_float = round(cm_float / 2.54)
inches = inches_float % 12
feets = int(inches_float // 12) % 3
yards = int(inches_float // 12) // 3

print(yards, "yd. ", feets, 'ft.', inches, 'in.')