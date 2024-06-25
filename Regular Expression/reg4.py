#www.mydomain.com--we want to extract data between two dots(.)
# .* (any character repeated any number of times)
# .*\.(.*)\..*-- to solve above question 

import re
s1=input("enter a string\n")
val=re.search(r".*\.(.*)\..*",s1)
if val:
    print(val.group(1))  #display the character between two dots  ,    group()--can be captured using paranthesis in regex
                                                                        # if we have 1 paranthesis then group(1)
                                                                        # if we have 2 paranthesis then group(2)
else:
    print("not matched")

#input : www.mydomain.com  
#output : mydomain