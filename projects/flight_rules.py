flight_altitude_int = int(input('Input flight altitude (ft): '))
airspace_class = input('Input airspace class: ')
visibility_int = int(input('Input visibility (km): '))
horizontal_cloud_int = int(input('Input horizontal cloud separation (ft): '))
vertical_cloud_int = int(input('Input vertical cloud separation (ft): '))

is_valid_bool = True
is_vfr = False

if (airspace_class != 'A' and \
    airspace_class != 'B' and \
    airspace_class != 'C' and \
    airspace_class != 'D' and \
    airspace_class != 'E' and \
    airspace_class != 'F' and \
    airspace_class != 'G') or \
    flight_altitude_int < 0 or \
    visibility_int < 0 or \
    horizontal_cloud_int < 0 or \
    vertical_cloud_int < 0:
    
    is_valid_bool = False

if is_valid_bool:
    if airspace_class != 'A':
        if flight_altitude_int >= 10000:
            if horizontal_cloud_int >= 1500 and \
                vertical_cloud_int >= 1000 and \
                visibility_int >= 8:

                is_vfr = True

        elif flight_altitude_int > 3000:
            if horizontal_cloud_int >= 1500 and \
                vertical_cloud_int >= 1000 and \
                visibility_int >= 5:

                is_vfr = True

        else:
            if airspace_class == 'F' or \
                airspace_class == 'G':

                if visibility_int >= 5:
                    is_vfr = True

            else:
                if horizontal_cloud_int >= 1500 and \
                    vertical_cloud_int >= 1000 and \
                    visibility_int >= 5:

                    is_vfr = True

if is_valid_bool:
    if is_vfr:
        print('Visual Flight Rules')
    else:
        print('Instrument Flight Rules')
else:
    print('Invalid input')