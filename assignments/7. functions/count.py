def count_case(s):
    upper_count, lower_count = 0,0
    for ch in s:
        if ch.islower():
            lower_count += 1
        elif ch.isupper():
            upper_count += 1
    return upper_count, lower_count

user_input = input("Enter a string: ")

upper, lower = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)