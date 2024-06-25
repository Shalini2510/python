"""class variable"""

# functions declared inside a class are called methods
# the first parameter to methods are assigned with the object reference
class Point:
    """this is an example class"""
    num_of_points = 0 # class variable accessed using class
    def __init__(self,xval,yval): # passing parameters to constructors
        self.x = xval # variables created with object reference are called instance attributes
        self.y = yval # variables created with object reference are called instance attributes
        Point.num_of_points += 1
    # example for instance method (bound method)
    def showValues(self,x1,y1):
        # display instance attributes
        print("parameters are:",self.x,self.y)
        print("this is an instance method")
        
    def showCount():
        print("number of points:",Point.num_of_points)

if __name__ == '__main__':
    p1 = Point(28,34)
    p1.showValues()
    p2 = Point(23,41)
    p2.showValues()