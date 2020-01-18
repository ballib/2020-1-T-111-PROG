num1 = int(input("First number: ")) 
num2 = int(input("Second number: ")) 
num3 = int(input("Third number: ")) 

min_int = num1

if num2 < min_int:
    min_int = num2

if num3 < min_int:
    min_int = num3

print("The minimum is: ", min_int) 