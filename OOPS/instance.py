"""Passing parameters to instance methods"""

# functions declared inside a class are called methods
# the first parameter to methods are assigned with the object reference
class Point:
    """this is an example class"""
    # example for instance method (bound method)
    def showValues(self,x1,y1):
        print("parameters are:",x1,y1)
        print("this is an instance method")

if __name__ == '__main__':
    p1 = Point()
    # get the documentation string
    p1.__doc__
    # call the object method
    p1.showValues(10,50)