import re
s1=input("enter a string\n")
#val=re.search(r"to*tal",s1)    #enter a string - toootal   output: matched
#val=re.search(r"to+tal",s1)    #enter a string m- tatal  output:  not matched
#val=re.search(r"https?://www.mydomain.com",s1)  #enter a string - www.mydomain.com  ouput-not matched
                                                #enter a string - https://www.mydomain.com  ouput-matched
                                                
val=re.search(r"http://w{3}.mydomain.com",s1)  #enter a string - https://ww.mydomain.com  ouput- not matched
                                                #enter a string - https://www.mydomain.com  ouput-matched
if val:
    print("matched")
else:
    print("not matched")