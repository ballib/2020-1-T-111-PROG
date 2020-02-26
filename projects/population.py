MAX_STATE_NAMES = 2

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None
    
def find_year_column(year_list, year):
    ''' Finds the column in the year_list corresponding to the given year '''
    for col in range(0, len(year_list)):
        if year == year_list[col]:
            return col
    return None # should not happen

def get_valid_years(file_stream):
    ''' Get the years that are in the header row of the file stream 
        Return the years as a list '''
    valid_years = []
    for line in file_stream:
        line_list = line.strip().split()
        # Only interested in the years and need to convert to ints
        valid_years = [int(i) for i in line_list[1:]] 
        break
    return valid_years

def get_population_state_tuple(line_list, valid_years, year_col):
    ''' Returns a tuples consisting of population and state by extracting it 
        from the given list '''
        
    if len(line_list) == len(valid_years) + MAX_STATE_NAMES: # then the state comprises more than one names
            state = line_list[0] + " " + line_list[1]
            population = line_list[year_col + 1]
    else:
        state = line_list[0]
        population = line_list[year_col]

    population = int(population)
    return (population,state)
        
def get_tuple_list(file_stream, valid_years, year_col):
    ''' Reads a file stream and returns a list of tuples for the given year 
        The header row in the file stream has already been read '''
    result_list = []
    for line in file_stream:
        line_list = line.strip().split()
        pop_state_tuple = get_population_state_tuple(line_list, valid_years, year_col)
        result_list.append(pop_state_tuple)
    return result_list

def get_year(valid_years):
    ''' Returns a valid year input by the user '''
    error_str = 'Invalid year!'
    
    while True:
        try:
            year = int(input("Enter year: "))
            if year in valid_years:
                return year
            print(error_str)
        except ValueError:
            print(error_str)

def print_min_max(population_tuples):
    ''' Prints the min and max population from the given tuple.
        Each tuple is of the form (population, state)
        Assumes that the list of tuples is sorted on the first item in each tuple '''

    print("Minimum: {}".format(min(population_tuples)))
    print("Maximum: {}".format(max(population_tuples)))

# Main program starts here
filename = input("Enter filename: ")
file_stream = open_file(filename)
if file_stream:
    valid_years = get_valid_years(file_stream)
    year = get_year(valid_years)
    year_column = find_year_column(valid_years, year)
    # Add 1 to year_column because the state info is in the first column
    population_tuples = get_tuple_list(file_stream, valid_years, year_column + 1)
    print_min_max(population_tuples)
    file_stream.close()
else:
    print("Filename {} not found!".format(filename))
