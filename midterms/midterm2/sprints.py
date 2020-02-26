
def parse_runner_data(line):
    runner_str, data_str = line.split(':')
    data_list = [float(i) for i in data_str.strip().split(' ')]
    return runner_str, data_list

def process_file(file_stream):
    ''' Process the file '''
    runner_best_list = []
    for line in file_stream:
        runner_str, data_list = parse_runner_data(line.strip())
        runner_best_list.append((runner_str, min(data_list)))
    
    return runner_best_list

def read_stream(filename):
    ''' Read stream from file '''
    try:
        return open(filename, "r")
    except FileNotFoundError:
        return None

def print_best_times(best_times_list):
    print('-- Best sprints --')
    for time in best_times_list:
        name_str, time_float = time
        print(f'{name_str}: {time_float}')

def main():
    ''' Main method '''
    filename = input("Enter name of file: ")
    file_stream = read_stream(filename)

    if file_stream:
        print_best_times(process_file(file_stream))
    else:
        print(f"File '{filename}' not found!")


main()