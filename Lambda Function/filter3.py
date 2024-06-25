#generate number upto 200. use filter and lamba to select elements divisible by 8.

numbers = [x for x in range(200)]

# filter using lambda function
num = list(filter(lambda x: x%8==0, numbers))

print(num)


#use list comprehension to generate numbers divisible by 8 between 0-200
nums=[x for x in range(200) if x%8==0]
print(nums)

