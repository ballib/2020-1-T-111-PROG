def range_test(n):
    if n in range(2,555):
        return True
    else :
        return False

num = int(input("Enter a number: "))
if range_test(num):
    print("{} is in range.".format(str(num)))
else:
    print("{} is outside the range!".format(str(num)))
    