a_str = input("Input a string: ")
output_str = ''
for w in a_str.split():
    if w.find('-') > 0:
        for sub in w.split('-'):
            output_str += sub[0].capitalize() + sub[1:] + '-'
        output_str = output_str[:-1] + ' '
    else:
        output_str += w[0].capitalize() + w[1:] + ' '
                
print(output_str[:-1])