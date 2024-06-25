#example of dict comprehension
key=['name','age','class']
values=['alex',6,'first']

d1={x:y for x,y in zip(key,values)}
print(d1)

#output--  {'name': 'alex', 'age': 6, 'class': 'first'}