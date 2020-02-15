m = int(input("Input the first integer: "))
n = int(input("Input the second integer: "))
gcd = 1

for i in range(1,m+1):
	if m % i == 0 and n % i == 0:
		gcd = i
print(gcd)
