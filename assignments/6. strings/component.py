
component_width_int = int(input('Input component width: '))
component_height_int = int(input('Input component height: '))
border_width = int(input('Input border width: '))
border_char = input('Input a border character: ')
message_str = input('Input a message to display: ')



if component_height_int % 2 == 0:
    vertical_center_int = int(component_height_int / 2) - 1
else:
    vertical_center_int = int(component_height_int / 2)

if abs(component_width_int - len(message_str)) % 2 == 0:
    message_start_x = int(component_width_int / 2 - len(message_str) / 2)
else:
    message_start_x = max(int(component_width_int / 2 - len(message_str) / 2) - 1, border_width)

for y in range(0, component_height_int):
    for x in range(0, component_width_int):
        if x < border_width or x > (component_width_int - border_width - 1) \
            or y < border_width or y > (component_height_int - border_width - 1):
            print(border_char, end=' ')
        else:
            if y == vertical_center_int: # vertically aligned to center
                if x >= message_start_x and x-message_start_x < len(message_str):
                    
                    print(message_str[x-message_start_x], end=' ')
                else:
                    print(' ', end=' ')
            else:
                print(' ', end=' ')
    print()


