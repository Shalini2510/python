#using custom function 

numbers = [x for x in range(50)]

def square(x):
    return x*x

# map using custom function
square_numbers = list(map(square,numbers))

print(square_numbers)