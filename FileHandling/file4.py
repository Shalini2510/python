fh = open('uk-500.csv','r')
count=0
while count<10:
    count +=1
    print(fh.readline())
fh.close()