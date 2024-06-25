"""python function name returns the function reference
Function Reference can be assigned to a variable,
the function can be called using the variable

Example for first class function"""

def square(x):
    return x*x

print(square(8)) # output will be 64

# print the function reference using function name
print(square) # function reference in hexadecimal form

# assign the function reference to a variable
ref1 = square

print(ref1) # function reference in hexadecimal form

# call the using the reference variable
print(ref1(8)) # output will be 64