#create an instance of a class bank account and then call withdraw method to ensure the script raises the custom exception

class BelowMinimumBalance(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __repr__(self):
        return self.msg


class BankAccount:
    def __init__(self,number,curBal,minBal):
        self.number = number
        self.curBal = curBal
        self.minBal = minBal

    def withdraw(self,amount):
        curBal = self.curBal
        self.curBal -= amount
        print(self.curBal)
        if self.curBal < self.minBal:
            #self.curBal = curBal
            raise BelowMinimumBalance("withdrwal below minimum balance is not allowed")
        return self.curBal
    
try:
    b = BankAccount(121,1500,500)
    b.withdraw(1200)
except BelowMinimumBalance as e:
    print(e)
