north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))

number_of_cars_at_once_int = 5

while north_int > 0 or \
    south_int > 0 or \
    east_int > 0 or \
    west_int > 0:

    longest_line_str = 'E/W' 
    
    if north_int + south_int >= east_int + west_int:
        longest_line_str = 'N/S'
    
    if longest_line_str == 'N/S':
        north_int = max(north_int - number_of_cars_at_once_int, 0)
        south_int = max(south_int - number_of_cars_at_once_int, 0)
    else:
        east_int = max(east_int - number_of_cars_at_once_int, 0)
        west_int = max(west_int - number_of_cars_at_once_int, 0)
    
    print(f'Green light on {longest_line_str}')

print('No cars waiting, the traffic jam has been solved!')