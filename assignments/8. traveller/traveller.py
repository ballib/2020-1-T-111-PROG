# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

# Summary
steps_taken_north_int = 0
steps_taken_south_int = 0
steps_taken_east_int = 0
steps_taken_west_int = 0
invalid_moves_int = 0

def get_next_cell(col_int, row_int, direction):
    ''' Gets the next cell given the direction '''
    if direction == NORTH:
        row_int -= 1
    elif direction == SOUTH:
        row_int += 1
    elif direction == EAST:
        col_int += 1
    elif direction == WEST:
        col_int -= 1
    
    return col_int, row_int


def can_move_to_cell(col, row, direction):
    ''' Checks if the move is valid '''
    next_col_int, next_row_int = get_next_cell(col, row, direction)

    # inside frame
    if 0 <= next_col_int <= 5 and 0 <= next_row_int <= 4: 
        # obstacles  
        if (next_col_int, next_row_int) != (1, 0) and \
            (next_col_int, next_row_int) != (2, 0) and \
            (next_col_int, next_row_int) != (1, 1) and \
            (next_col_int, next_row_int) != (2, 1) and \
            (next_col_int, next_row_int) != (1, 3) and \
            (next_col_int, next_row_int) != (3, 3):
            
            return True

    return False

def is_at_destination(col, row):
    ''' Return true is player is in the destination street'''
    return col == 5

def increment_counters(direction_str):
    ''' Increment the counters used in the summary '''
    global steps_taken_north_int
    global steps_taken_south_int
    global steps_taken_east_int
    global steps_taken_west_int
    global invalid_moves_int

    if direction_str == NORTH:
        steps_taken_north_int += 1
    elif direction_str == SOUTH:
        steps_taken_south_int += 1
    elif direction_str == EAST:
        steps_taken_east_int += 1
    elif direction_str == WEST:
        steps_taken_west_int += 1
    else:
        invalid_moves_int += 1

def try_move(col_int, row_int, direction_str):
    ''' Tries to move to the specified cell '''
    if can_move_to_cell(col_int, row_int, direction_str):
        col_int, row_int = get_next_cell(col_int, row_int, direction_str)
        increment_counters(direction_str)
    else:
        increment_counters('')
    
    return col_int, row_int

def print_summary_row(key_str, value_str):
    ''' Formats and prints a summary row '''
    print('{:<10}{:>4}'.format(f'{key_str}:', value_str))

def print_summary():
    ''' Prints the summary '''
    print('You have reached the destination!')
    print_summary_row('NORTH', steps_taken_north_int)
    print_summary_row('SOUTH', steps_taken_south_int)
    print_summary_row('EAST', steps_taken_east_int)
    print_summary_row('WEST', steps_taken_west_int)
    print_summary_row('INVALID', invalid_moves_int)

    total_moves_int = steps_taken_north_int + steps_taken_south_int + \
        steps_taken_east_int + steps_taken_west_int + invalid_moves_int
    print_summary_row('TOTAL', total_moves_int)

def print_location(col_int, row_int):
    ''' prints the location '''
    print(f'You are located at ({col_int}, {row_int})')


def parse_input(col_int, row_int, direction_str):
    ''' Parses the input string '''
    for d in direction_str:
        col_int, row_int = try_move(col_int, row_int, d.lower())
        if is_at_destination(col_int, row_int):
            return col_int, row_int, True
    return col_int, row_int, False

col_int = 0
row_int = 0
at_destination_bool = False

while not at_destination_bool:
    direction_str = input('Enter direction: ')
    col_int, row_int, at_destination_bool = parse_input(col_int, row_int, direction_str)
    if at_destination_bool:
        print_summary()
    else:
        print_location(col_int, row_int)
