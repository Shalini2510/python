"""destructors"""

# functions declared inside a class are called methods
# the first parameter to methods are assigned with the object reference
class Point:
    """this is an example class"""
    def __init__(self,xval,yval): # passing parameters to constructors
        self.x = xval # variables created with object reference are called instance attributes
        self.y = yval # variables created with object reference are called instance attributes
        
    # example for instance method (bound method)
    def showValues(self):
        # display instance attributes
        print(f"x-val:{self.x}, y-val:{self.y}")
      
        
    def __del__(self):
        print("destructor called")

if __name__ == '__main__':
    p1 = Point(28,34)
    print(p1)
    
    # explicitly delete to invoke constructor
    del p1