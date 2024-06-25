# MRO - Method Resolution Order to resolve the version to be invoked in case same function being implemented in multiple parent classe
#gives order of execution 
#given as a class property i.e. ---> __mro__
'''class A:
    def printString(self):
        print("from A")

class C:
    def printString(self):
        print("from C")

class B(A,C):   #output: from A because A class is first
    pass

obj=B()
obj.printString()'''


'''class A:
    def printString(self):
        print("from A")

class C:
    def printString(self):
        print("from C")

class B(C,A):  #output: from C because C class is first
    pass

obj=B()
obj.printString()'''

class E:
     def printString(self):
        print("from E")

class A:
    def printString(self):
        print("from A")
        
class C(E):
    pass
    #def printString(self):
    #    print("from C")
        
        
class B(C,A):
    pass

obj=B()
obj.printString()
print(B.__mro__)  #returns order of execution
