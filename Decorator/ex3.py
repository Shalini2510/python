def display(name):
    return f"welcome {name} to python"
#welcome bob to python

def sdecorator(f):   #f--reference to display
    def d(name):   #parameter passed to display
        return "<s>{}</s>".format(f(name))    #f(name) -- display(name)
    return d

print(display('bob'))
display = sdecorator(display)
print("after passing to decorator.....")
print(display('bob'))

#output:
# welcome bob to python
# after passing to decorator.....
# <s>welcome bob to python</s>
