class A:
    def printString(self):
        print("from A")
class B(A):
    def displayString(self):
        print("from child method")

    def printString(self):    #reimplementation of parent class method
        print("from B")

obj=B()
obj.displayString()
obj.printString()