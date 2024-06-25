class MyError(Exception):
     def __init__(self,value):
         self.value=value
     def __repr__(self):
         return self.value
try:
     raise MyError("this is test exception")
except MyError as e:
     print ("Error occured", e.value)