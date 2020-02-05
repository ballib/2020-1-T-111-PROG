num_int = int(input("Enter an integer: "))
largest_int = 0
even_sum_int = 0
odd_sum_int = 0
cum_total_int = 0

while num_int > 0:
    if num_int > largest_int:
        largest_int = num_int

    if num_int % 2 == 0:
        even_sum_int += num_int 
    else:
        odd_sum_int += num_int
    
    cum_total_int = cum_total_int + num_int
    print("Cumulative total:", cum_total_int)
    num_int = int(input("Enter an integer: "))

if largest_int != 0:
    print("Largest number:", largest_int)
    print("Sum of even numbers:", even_sum_int)
    print("Sum of odd numbers:", odd_sum_int)
