LIST_MAX_SIZE = 7

def try_parse_int(input_str):
    try:
        return int(input_str)
    except ValueError:
        return None

def add_to_list(input_float, list_int):
    list_int.insert(0, input_float)

    if len(list_int) > LIST_MAX_SIZE:
        list_int.pop()

def print_status(list_int):
    print(list_int)
    if len(list_int) < LIST_MAX_SIZE:
        print('Not enough data to print moving average...') 
    else:
        print(f'Floating average is {sum(list_int)/len(list_int):.2f}')

def main():
    list_float = []
    while True:
        input_str = input('Enter a number: ')
        if input_str == 'q':
            break

        input_float = try_parse_int(input_str)

        if input_float == None:
            print(f"Failed to convert '{input_str}' to an int!")
        else:
            add_to_list(input_float, list_float)
            print_status(list_float)

main()