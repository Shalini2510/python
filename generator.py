""" Generator - Function working as iterable. 'yield' is the keyword used for converting a function as iterable
Example for Generator"""#returns 1 element at a given time to memory
# function becomes iterable as 'yield' keyword has been used inside
def genseq():
    yield 1
    yield 2
    yield 3

# iterate over the function
for num in genseq():
    print(num)
    