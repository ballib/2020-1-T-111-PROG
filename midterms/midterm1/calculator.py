left_int = int(input("Input number: "))  # input number
op = input("Input operation: ")          # input operation
right_int = int(input("Input number: ")) # input number

result_int = None
if op == "+":
    result_int = left_int + right_int
elif op == "-":
    result_int = left_int - right_int
elif op == "*":
    result_int = left_int * right_int
elif op == "/":
    result_int = round(left_int / right_int)


print(f"{left_int} {op} {right_int} = {result_int}")