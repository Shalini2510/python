#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

"""Example for list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)"""
#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#ouput--['apple', 'banana', 'mango']
#only words containing 'a' 