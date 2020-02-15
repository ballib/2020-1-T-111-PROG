def safe_input(prompt='', a_type=str):
    ''' An input function that only accepts the specified type of input '''
    while True:
        try:
            i = a_type(input(prompt))
            return i
        except ValueError:
            print("Error: please enter a value of", a_type)
        
# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))

