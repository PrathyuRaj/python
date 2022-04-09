# addition program using constructor


class Addition:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printvalue(self):
        print(self.num1+self.num2)
ad1=Addition(10,55)
ad1.printvalue()