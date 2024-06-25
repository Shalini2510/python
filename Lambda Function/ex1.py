'''lambda is a keyword for creating anonymous functions
lambda returns function reference
syntax for lambda:
lambda arguments : expression
lambda p1,p2,p3,....: body of lambda
The last evaluated expression is returned in lambda function'''

# defining a lambda function
ref2 = lambda x: x*x

# now ref2 has the reference of lambda
print(ref2) # lambda function reference in hexadecimal form

# calling the lambda function
print(ref2(8)) # output will be 64