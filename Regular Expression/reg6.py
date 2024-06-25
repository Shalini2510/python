#[]-- character class
#'hello\s[A-Za-z0-9_]   
import re
s1=input("enter a string\n")
val=re.search(r'hello\s[\w]',s1)   #\w--[A-Za-z0-9_]

if val:
    print("matched")
else:
    print("not matched")


