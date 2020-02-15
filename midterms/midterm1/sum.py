sum_int = 0
num = 0
while sum_int <= 100:
    num = input("Input a number: ")
    if num == "q":
        break
    else:
        sum_int += int(num)
    
print('Sum:', sum_int)