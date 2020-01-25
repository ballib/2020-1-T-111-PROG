lower_int = int(input('Input lower: '))
upper_int = int(input('Input upper: '))
step_int = int(input('Input step size: '))

counter = lower_int
while counter < upper_int:
    print(counter, end=' ')
    counter += step_int
