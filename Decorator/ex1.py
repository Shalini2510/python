
#write a decorator which adds ** on both sides of input of function add
#add(2,3)--**5**

def sdecorator(f):   #f--reference to display
    def d(a,b):   #parameter passed to display
        return "**{}**".format(f(a,b))    #f(name) -- display(name)
    return d
@sdecorator
def add(a,b):
    return a+b
print(add(2,3))

#output: **5**