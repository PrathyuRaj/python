class Addition:
    def sum(self,num1,num2):#(sum=method,attributes=num1,num2)
        self.num1=num1
        self.num2=num2
    def printsum(self):
        print(self.num1+self.num2)
ad=Addition()
ad.sum(4,9)
ad.printsum()