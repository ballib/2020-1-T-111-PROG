num_int = int(input('Input number: '))
err_int = int(input('Input accuracy: '))

delta = 1
square_root_float = num_int / 2 # initial guess

'''
    iterate while the previous guess and the updated guess
    still differs with the given number of accuracy
'''
while delta > 0: 
    temp = round((square_root_float + num_int / square_root_float) / 2, err_int)
    delta = abs(temp - square_root_float)
    square_root_float = temp

print('The square root of {} is {}'.format(num_int, square_root_float))
