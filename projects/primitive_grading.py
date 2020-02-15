a_min_weight_int = 0
a_max_weight_int = 3
a_current_weight_int = 0

b_max_weight_int = 8
b_current_weight_int = 0

c_max_weight_int = 15
c1_current_weight_int = 0
c2_current_weight_int = 0

a_target_batch_size_int = 30
b_target_batch_size_int = 40
c_target_batch_size_int = 50

reject_weight_int = 0

while a_current_weight_int < a_target_batch_size_int or \
    b_current_weight_int < b_target_batch_size_int or \
    c1_current_weight_int < c_target_batch_size_int or \
    c2_current_weight_int < c_target_batch_size_int:

    input_str = input('Enter piece weight: ')
    if input_str == 'q':
        break

    piece_weight_int = int(input_str)
    

    if a_min_weight_int < piece_weight_int <= a_max_weight_int and \
        a_current_weight_int < a_target_batch_size_int:
        a_current_weight_int += piece_weight_int
        print('-> Gate A')
        
    elif a_max_weight_int < piece_weight_int <= b_max_weight_int and \
        b_current_weight_int < b_target_batch_size_int:
        b_current_weight_int += piece_weight_int
        print('-> Gate B')

    elif b_max_weight_int < piece_weight_int <= c_max_weight_int:
        
        if c1_current_weight_int < c_target_batch_size_int:
            c1_current_weight_int += piece_weight_int
            print('-> Gate C1')

        elif c2_current_weight_int < c_target_batch_size_int:
            c2_current_weight_int += piece_weight_int
            print('-> Gate C2')

        else:
            reject_weight_int += piece_weight_int
            print('-> Reject!')

    else:
        reject_weight_int += piece_weight_int
        print('-> Reject!')
    
    
else:
    print('All orders completed!')

print()
print('-- Run results --')
print(f'Gate A: {a_current_weight_int} kg.')
print(f'Gate B: {b_current_weight_int} kg.')
print(f'Gate C1: {c1_current_weight_int} kg.')
print(f'Gate C2: {c2_current_weight_int} kg.')
print(f'Reject: {reject_weight_int} kg.')