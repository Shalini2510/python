def calculateinterest(p,n,r):
    if r<=0:
        raise ValueError
    if n<=0:
        raise ValueError
    
    return p*n*r/100

try:
    calculateinterest(1000,2,-8)
except ValueError:
    print("negative value not accepted")