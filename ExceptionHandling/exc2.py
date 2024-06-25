import sys
try:
    x=input("enter a number")
    x=int(x)
    print (x)
except ValueError:
    print ("some error", sys.exc_info())
print("continue the script...")