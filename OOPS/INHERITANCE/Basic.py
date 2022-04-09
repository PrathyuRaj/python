# Single inheritance

class A: #base class,parent class,superclass
    def printa(self,num1):
        self.num1=num1
        print("inside print a",self.num1)
class B(A): #childclass,subclass,derivedclass
    def printb(self,num):
        self.num=num
        print("inside print b",self.num)
        print(self.num)
a=A()
a.printa(4)
b=B()
b.printa(7)

