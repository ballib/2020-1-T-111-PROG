d1 = int(input("Input first dice: ")) 
d2 = int(input("Input second dice: ")) 

if d1 < 1 or d1 > 6 or d2 < 1 or d2 > 6:
    print("Invalid input")
else:
    sum = d1 + d2
    if sum == 2:
        print("Snake eyes")
    elif sum == 12:
        print("Dozen")
    else:
        print(sum)