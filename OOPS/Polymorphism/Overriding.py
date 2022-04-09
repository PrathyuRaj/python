#same method name same numbr of arguments

class A:
    def printdata(self,num):
        self.num=num
        print("inside A class",self,num)

class B(A):
    def printdata(self,num2):
        self.num2=num2
        print("inside B class",self,num2)
b1=B()
b1.printdata(4)
