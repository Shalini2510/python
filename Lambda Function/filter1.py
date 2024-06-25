#filter is used for extracting elements from a sequence using a criterion/criteria
'''filter - Takes 2 arguments. Returns a filter object which can be type casted to a list
1st param is a function reference. The function returns either True of False
2nd param is a sequence (or) sequences
Passes the element(s) from the sequence to the function referred by 1st param
the element is added to filter object if the function returns True'''

numbers = [x for x in range(50)]

# filter using lambda function
even_numbers = list(filter(lambda x: x%2==0, numbers))

print(even_numbers)

#lamda returns lambda function reference