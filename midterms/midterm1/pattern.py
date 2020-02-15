rows_int = int(input("Enter number of rows: "))
columns_int = int(input("Enter number of columns: "))

for i in range(rows_int):
    for j in range(columns_int):
        print("*", end=" ")
    print()