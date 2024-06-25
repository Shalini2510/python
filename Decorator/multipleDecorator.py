def vdecorator(f):
    def d(name):   #parameter passed to display
        return "<div>{}</div>".format(f(name))    #f(name) -- display(name)
    return d

def sdecorator(f):   #f--reference to display
    def d(name):   #parameter passed to display
        return "<s>{}</s>".format(f(name))    #f(name) -- display(name)
    return d
 
@vdecorator     
@sdecorator
def display(name):
    return f"welcome {name} to python"

print(display('bob')) 

#output:
#<div><s>welcome bob to python</s></div>