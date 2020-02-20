front_space_float = None
back_space_float = None
left_space_float = None
right_space_float = None
precipitation_str = "None"

# Constants
SENSOR_FRONT = "SF"
SENSOR_BACK = "SB"
SENSOR_LEFT = "SL"
SENSOR_RIGHT = "SR"
PRECIPITATION = "P"
PRECIPITATION_NONE = "NONE"
PRECIPITATION_MIST = "MIST"
PRECIPITATION_DRIZZLE = "DRIZZLE"
PRECIPITATION_RAIN = "RAIN"
NO_DATA = "NO DATA"
CLEAR_ROAD = "CLEAR ROAD"

def log_error(error):
    ''' Log error message '''
    print(f'Error: {error}')

def log_info(info):
    ''' Log info message '''
    print(f'Info: {info}')

def process_message_parts(line):
    ''' Processes the message and extracts the parts '''
    global front_space_float
    global back_space_float
    global left_space_float
    global right_space_float
    global precipitation_str

    for part in line.split(';'):
        key_str, value_str = part.split(':')

        try:
            if key_str == SENSOR_FRONT:
                front_space_float = float(value_str)

            elif key_str == SENSOR_BACK:
                back_space_float = float(value_str)

            elif key_str == SENSOR_LEFT:
                left_space_float = float(value_str)

            elif key_str == SENSOR_RIGHT:
                right_space_float = float(value_str)

            elif key_str == PRECIPITATION:
                if value_str == PRECIPITATION_NONE or \
                    value_str == PRECIPITATION_MIST or \
                    value_str == PRECIPITATION_DRIZZLE or \
                    value_str == PRECIPITATION_RAIN:
                    precipitation_str = value_str

            else:
                log_error(f'Unknown message part {key_str}.')

            log_info(f"Parsed part: {key_str:<2} with value: {value_str}")

        except:
            log_error(f"Failed to parse part '{part}'")
    

def print_proximity(direction_str, distance_int):
    ''' Prints the proximity '''
    value = ''
    if distance_int == None:
        value =  NO_DATA
    elif distance_int >= 0:
        value =  f'{distance_int}m'
    else:
        value = CLEAR_ROAD

    print_state_row(direction_str, value)

def print_state_row(key, value):
    ''' Prints a formatted row '''
    print('{:<15}{:>12}'.format(key + ':', value))

def print_state():
    ''' Prints the current state '''
    print()
    print('------ CURRENT STATE ------')
    print_proximity('FRONT', front_space_float)
    print_proximity('BACK', back_space_float)
    print_proximity('LEFT', left_space_float)
    print_proximity('RIGHT', right_space_float)
    print_state_row('PRECIPITATION', precipitation_str)

def parse_sensor_data(line):
    process_message_parts(line)

def process_file(file_stream):
    ''' Process the file '''
    for line in file_stream:
        parse_sensor_data(line.strip())

def read_stream(filename):
    ''' Read stream from file '''
    try:
        return open(filename, "r")
    except FileNotFoundError:
        return None

def main():
    ''' Main method '''
    filename = input("Enter name of file: ")
    file_stream = read_stream(filename)

    if file_stream:
        process_file(file_stream)
        print_state()
    else:
        print(f"File '{filename}' not found!")


main()