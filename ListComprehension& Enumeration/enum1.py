'''Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.

This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

enumerate optionally takes 2nd argument to specify the start index. Default start index is zero'''

# Python program to illustrate
# enumerate function in loops
list1 = ["eat", "sleep", "repeat"]
  
# printing the tuple elements directly
#for idx,ele in enumerate(list1):
#    print (idx,ele)

#ouput-- 0 eat
#        1 sleep
#        2 repeat

for idx,ele in enumerate(list1,100):
    print (idx,ele)


#ouput-- 100 eat
#        101 sleep
#        102 repeat