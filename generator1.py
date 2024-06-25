# generate series of numbers using a function
#sum of all integers from 1 to n

def findsum(n):
    nums = 0
    while nums < n:
        nums += 1
        yield nums

        
# obtain the sum 'n' numbers
# sum is a built-in function accepts an iterable as argument and returns
# sum of elements in sequence
# since findsum is also a iterable, it is passed to sum to get sum elements generated
sum_of_numbers = sum(findsum(20))
print(sum_of_numbers)

#output = 210