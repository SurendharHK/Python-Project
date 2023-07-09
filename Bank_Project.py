class Account:
    accno=0
    balance=0
    def __init__(self,accno,balance):
        self.accno=accno
        self.balance=balance

class SBAccount(Account):
    accno=0
    balance=0
    def __init__(self,accno,balance):
        super().__init__(accno,balance)
        self.accno=accno
        self.balance=balance
        print("your account created with customer id",Customer.cust_id,"and account no", Customer.accno,"with depoisted amount of" ,self.balance)
    def deposit(self,amount):
        if(amount > 0):
            print("your old balance: ",self.balance)
            self.balance=self.balance+amount
            print("****succesfully deposited****")
            print("your current balance: ",self.balance)
        else:
            print("Enter the valid amount")
    def withdraw(self,amount):
        if(1000 < self.balance - amount):
            print("your old balance: ",self.balance)
            self.balance=self.balance-amount
            print("*****succesfully*****")
            print("your current balance: ",self.balance)
        else:
            print("your current balance is low!")

    def calc_interest(self):
        interest = (self.balance*1*4)/100
        print("your old balance",self.balance)
        self.balance=self.balance+interest
        print("your current balance",self.balance)

class FDAccount(Account):
    accno=0
    balance=0
    period=0
    def __init__(self,accno,balance,period):
        super().__init__(accno,balance)
        self.accno=accno
        self.balance=balance
        self.period=period
    def calc_interest(self):
        interest = (self.balance*selfperiod*8.25)/100
        return interest
    def close(self):
        self.balance=self.balance+self.calc_interest()
        print("your Maturity amount: ",self.balance)

class Customer:
    cust_id=0
    accno=11011
    def __init__(self,name,address):
        self.name = name
        self.address = address
        sbaccount = None
        fdaccount = None
    def createAccount(self,type):
        if type==0:
            amount = int(input("Enter the amount to deposit--------->"))
            self.sbaccount = SBAccount(self.accno,amount)
            
            Customer.accno=Customer.accno+11
            Customer.cust_id=Customer.cust_id+1

        elif type==1:
            amount = int(input("Enter the amount to be deposited----->"))
            period = int(input("Enter the period--------------------->"))
            self.fdaccount= FDAccount(self.accno,amount,period)
            Customer.accno=Customer.accno+11
            Customer.cust_id=Customer.cust_id+1
    def transaction(self,type):
        if type==0:
            print("****************************************")
            choice = int(input("Enter 1 for depoist \n Enter 2 for withdraw \n Enter 3 for calcualte interest\n"))
            if choice==1:
                print("****************************************")
                amount = int(input("Enter the amount to deposit----->"))
                self.sbaccount.deposit(amount)
            elif choice ==2:
                print("****************************************")
                amount= int(input("Enter the amount to withdraw------>"))
                self.sbaccount.withdraw(amount)
            elif choice ==3:
                self.sbaccount.calc_interest()
            else:
                print("Enter valid choice")

        elif type==1:
            print("****************************************")
            choice = int(input("Enter 1 for fd close---->"))
            if choice==1:
                self.fdaccount.close()
            else:
                print("Enter valid choice")       


if __name__=='__main__':

    l=[]
    i=0

    while True:
        print("****************************************")
        print("Enter 1---- for create account")
        print("Enter 2---- for transaction")
        print("Enter 3---- for exit")
        print("****************************************")
        choice =int(input("Enter choice------>"))
        if choice==1:
            print("****************************************")
            ch=int(input("Enter 0 for sb account \nEnter 1 for fd account\n"))
            print("****************************************")
            if ch==0:
                print("****************************************")
                name=input("Enter a name--------------->")
                address = input("Enter a address------->")
                print("****************************************")
                l.append(Customer(name,address))
                l[i].createAccount(ch)
                i+=1
            elif ch==1:
                print("****************************************")
                name=input("Enter a name--------------->")
                address = input("Enter a address------->")
                print("****************************************")
                l.append(Customer(name,address))
                l[i].createAccount(ch)
                i+=1
            else:
                break

        elif choice== 2:
            print("****************************************")
            ch=int(input("Enter 0 for sb account transaction \nEnter 1 for fd account\n"))
            print("****************************************")
            if ch==0:
                cust = int(input("Enter customer id----->"))
                l[cust].transaction(ch)
            elif ch==1:
                cust=int(input("Enter customer id-------->"))
                l[cust].transaction(ch)
                   
        elif choice== 3:
            break
                        
                
    
    
    
    
    
