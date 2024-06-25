'''The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

Use that function definition to make a function that always doubles the number you send in:

Example'''

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#myfunc(10)---function call
print(myfunc)  #function name return the function reference

#output = 22
