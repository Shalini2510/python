

"""Example for nested function"""
def f(x):
    def g(y):
        return y*y
    return x+g(x)

# calling the nested function
retval = f(10) 
print(retval) # output will be 110