#use list comprehension to generate numbers divisible by 8 between 0-200
nums=[x for x in range(200) if x%8==0]
print(nums)