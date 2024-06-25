"""Example class"""

# functions declared inside a class are called methods
# the first parameter to methods are assigned with the object reference
class Point:
    """this is an example class"""
    # example for instance method (bound method)
    def showValues(self):
        print("this is an instance method")

if __name__ == '__main__':
    p1 = Point()
    # get the documentation string
    print(p1.__doc__)
    # call the object method
    p1.showValues() # p1.showValues(p1)