def is_prime(n):
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True
    
num = int(input("Input an integer greater than 1: "))

if is_prime(num):
    print("{:d} is a prime".format(num))
else:
    print("{:d} is not a prime".format(num))