class Point:
    """this is an example class"""
    def __init__(self,xval,yval): # passing parameters to constructors
        self.x = xval # variables created with object reference are called instance attributes
        self.y = yval # variables created with object reference are called instance attributes
        
    # example for instance method (bound method)
    def showValues(self):
        # display instance attributes
        print(f"x-val:{self.x}, y-val:{self.y}")
    def __repr__(self):
        return f"x-val:{self.x}, y-val:{self.y}"
p1=Point(10,20)
print(p1)