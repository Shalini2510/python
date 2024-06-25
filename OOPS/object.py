"""Display object reference"""

# functions declared inside a class are called methods
# the first parameter to methods are assigned with the object reference
class Point:
    """this is an example class"""
    # example for instance method (bound method)
    def showValues(self):
        # self has the object reference
        print(self)
        print("this is an instance method")

if __name__ == '__main__':
    p1 = Point()
    # get the documentation string
    p1.__doc__
    # get the object reference by printing the object
    print(p1)
    # call the object method
    p1.showValues()