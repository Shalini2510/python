# match - takes 3 arguments. 3rd argument is optional
#         1st param - regular expression
#         2nd param - string to be matched
#         3rd param - flags
#         matches a single line.
#         return match object on success or False on failure
#
# search - takes 3 arguments. 3rd argument is optional
#         1st param - regular expression
#         2nd param - string to be matched
#         3rd param - flags
#         matches a against multiple lines
#         return match object on success or False on failure
########################################################
import re

s1="the name of the employee is Bob Smith and his designation is developer"

#match
#search
# r --- refers it is string literal and used to avoid interpretation
val = re.search(r'(\b[A-Z][a-z]+\s[A-Z][a-z]+\b)',s1)
if val:
    print(val.group(1))