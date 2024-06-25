#[\b[A-Z][a-z]+\s[A-Z][a-z]+\b]
#starts with A-Z followed by any number of char btwn a-z then a space then A-Z followed by any number of char btwn a-z 
import re
s1="the name of the employee is Bob Smith and his designation is developer"

p=re.compile(r'(\b[A-Z][a-z]+\s[A-Z][a-z]+\b)')   #returns a regex object 

val=p.search(s1)

if val:
    print(val.group(1))
else:
    print("not matched")