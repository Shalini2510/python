fh = open('hello.txt','r')
for num,line in enumerate(fh.readlines(),1):
    if num>=10 and num<=20:
        print(line)
fh.close()