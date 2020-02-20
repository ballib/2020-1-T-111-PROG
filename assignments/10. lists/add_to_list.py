def triple_list(a_list):
    ''' Returns a new list with 3 copies of every value in the given list '''
    return a_list * 3

def read_string():
    ''' Prompts for an input string and returns it '''
    input_str = input('Enter value to be added to list: ')
    return input_str

def populate_list(a_list):
  a_string = read_string()
  while a_string != 'exit':
      a_list.append(a_string)
      a_string = read_string()

def print_list(a_list):
    for item in a_list:
        print(item)

# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)
print_list(new_list)

