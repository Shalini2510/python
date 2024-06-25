#decorator-- technique to improve function without modifying code inside it

def sdecorator(f):   #f--reference to display
    def d(name):   #parameter passed to display
        return "<s>{}</s>".format(f(name))    #f(name) -- display(name)
    return d
#<s>welcome bob to python</s>       
@sdecorator
def display(name):
    return f"welcome {name} to python"

print(display('bob'))   #welcome bob to python 