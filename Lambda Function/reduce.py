#The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned
# in the sequence passed along.
#reduce takes sequence as an argument and returns a single value
#reduce can be imported from functools


'''Working :  

1. At first step, first two elements of sequence are picked and the result is obtained.
2. Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
3. This process continues till no more elements are left in the container.
4. The final returned result is returned and printed on console.'''

from functools import reduce
numbers=[x for x in range(1,20)]
#find the sum of numbers from 1-20
#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
#1+2
#3+3
#6+4

total=reduce(lambda x,y: x+y, numbers)
print(total)