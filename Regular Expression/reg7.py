#[\b[A-Z][a-z]+\s[A-Z][a-z]+\b]
#starts with A-Z followed by any number of char btwn a-z then a space then A-Z followed by any number of char btwn a-z 
import re
s1=" hi hello world"
val=re.search(r'\bhello\b',s1)   #\b-- seperate word 

if val:
    print("matched")
else:
    print("not matched")

# if we give input - " hi hello world"  then output--matched
# if we give input - " hi helloworld"  then output--not matched