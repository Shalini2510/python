#Closure is nested function that returns the reference of inner function

"""Example for closure"""
def f(x):
    def g(y):
        return y*y
    return g

# The return value of f is reference of inner function 'g'
retval = f(10)

# retval has the reference of inner function of 'f' i.e., 'g'
print(retval) # output will be <function f.<locals>.g at 0x7f3fe0171e60>

print(retval())  #call the inner function g using its reference