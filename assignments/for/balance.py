balance_float = float(input("Enter initial balance: "))
rate_float = float(input("Enter interests (%): "))
years_int = int(input("Enter number of years: "))

for year in range(1, years_int + 1):
    balance_float = round(balance_float * (1 + rate_float / 100), 1)

print(f"Total balance: {balance_float}")