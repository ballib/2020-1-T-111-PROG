def find_max(a,b):
    if a > b:
        return a
    else:
        return b

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
maximum = find_max(first,second)
print("Maximum: ", maximum)