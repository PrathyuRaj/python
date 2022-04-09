#



class Bank:
    bname="SBI" #(static variable)
    def ac_create(self,accountno, account_holder_name):
        self.accountno=accountno
        self.account_holder_name=account_holder_name
        self.minbalnc=1000
        self.balance=self.minbalnc
    def deposit(self,amt):
        self.amt=amt
        self.balance=self.balance+self.amt
        print(" your" ,Bank.bname,"ac credited with amount",self.amt)  #(static variable calld with class name)
        print("your total balance is",self.balance)
    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.balance:
            print("inufficient balance")
        else:
            self.balance=self.balance-self.amnt
            print("your",Bank.bname,"debited with amount",self.amnt)
            print("your bank balance",self.balance)
user1=Bank()
user1.ac_create(1222,"ammu")
# a=input("enter ypur amnt")
user1.deposit(100)                        #OR   as input from  # a=input("enter ypur amnt") give befr functn call\

# user1.withdraw(500)

