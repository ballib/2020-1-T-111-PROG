num_float = float(input('Input a decimal: '))

divisor_int = 1
fraction_float = 0
maximum_number_of_iterations_int = 100
fraction_found_bool = False

while divisor_int < maximum_number_of_iterations_int:
    divisor_int += 1
    fraction_float = 1 / divisor_int
    if fraction_float == num_float:
        fraction_found_bool = True
        break

if fraction_found_bool:
    print(f'The fraction is 1/{divisor_int}.')
else:
    print('Fraction not found!')