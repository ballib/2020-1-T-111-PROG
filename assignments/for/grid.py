num_int = int(input('Input number: '))

for y in range(num_int - 1, -1, -1):
    for x in range(0, num_int):
        print(f'({x},{y})', end=' ')
    print()