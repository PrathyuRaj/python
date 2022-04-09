# MULTIPLE INHERITANCE(MORE THAN ONE PARENT)


class A:  #PARENT CLASS
    def printA(self):
        print("inside a")
class B:   #PARENT CLASS
    def printB(self):
        print("inside B")
class D:  #PARENT CLASS
    def printD(self):
        print("inside D")
class C(A, B, D):  #CHILDCLASS
    def printC(self):
        print("inside c")


c1=C()
c1.printA()
c1.printB()
c1.printC()
c1.printD()