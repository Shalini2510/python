"""Creating constructors"""

# functions declared inside a class are called methods
# the first parameter to methods are assigned with the object reference
class Point:
    """this is an example class"""
    def __init__(self):
        self.x = 10 # variables created with object reference are called instance attributes
        self.y = 20 # variables created with object reference are called instance attributes
        
    # example for instance method (bound method)
    def showValues(self,x1,y1):
        # display instance attributes
        print("instance attributes:",self.x,self.y)
        print("this is an instance method")

if __name__ == '__main__':
    p1 = Point()
    # get the documentation string
    p1.__doc__
    # call the object method
    p1.showValues(10,50)