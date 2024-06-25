numbers = [2,3,4,5,6,7,8,10]

newlist = [x**2 for x in numbers if x%2==0]

print(newlist)


#output - [4, 16, 36, 64, 100]    
#gives square of 2,4,6,8,10