#map is used for transforming a sequence from one form to another
'''map - Takes 2 arguments. Returns a filter object which can be type casted to a list
1st param is a function reference.
2nd param is a sequence (or) sequences
Passes the element(s) from the sequence to the function referred by 1st param
the return value of the function is added to map object'''


"""Example for map"""

numbers = [x for x in range(50)]

# map using lambda function
square_numbers = list(map(lambda x: x*x,numbers))

print(square_numbers)