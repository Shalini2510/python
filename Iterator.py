'''Iterator - Has next function. Fetches one element to memory at a given point of time

Raises StopIteration error after accessing all elements'''

#example of iterator

list1 = [10,20,30,40,50]

ia = iter(list1)

# fetch some more element
print(next(ia)) # or print(ia.__next__())  return 1 element at a time
print(next(ia)) # or print(ia.__next__())
print(next(ia)) # or print(ia.__next__())
print(next(ia)) # or print(ia.__next__())

