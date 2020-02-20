def dot_product(v1, v2):
    summa = 0
    for i in range(len(v1)):
        summa += v1[i]*v2[i]
    return summa

def input_vector(size):
    vector = []
    for i in range(size):
        elem = float(input("Element no {}: ".format(i+1)))
        vector.append(elem)
    return vector

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
vector1 = input_vector(size)
vector2 = input_vector(size)
print("Dot product is:", dot_product(vector1, vector2))