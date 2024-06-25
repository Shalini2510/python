#decorator-- technique to improve function without modifying code inside it


def display(name):
    return f"welcome {name} to python"
#welcome bob to python

def sdecorator(f):   #f--reference to display
    def d(name):   #parameter passed to display
        return "<s>{}</s>".format(f(name))    #f(name) -- display(name)
    return d
#<s>welcome bob to python</s>      

mydisplay= sdecorator(display)
print(mydisplay) #gives the reference of inner function 'd'
print(mydisplay('bob'))