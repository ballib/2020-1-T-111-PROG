def list_to_tuple(a_list):
    try:
        a_list = [int(i) for i in a_list]
        a_tuple = tuple(a_list)
        return(a_tuple)
    except ValueError:
        print("Error. Please enter only integers.")
        return ()

# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)