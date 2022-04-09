class Person:
    def  setvalue(self,name,age1):
        self.name=name
        self.age=age1
    def printvalue(self):
        print(self.name)
        print(self.age)
pe1=Person()
pe1.setvalue("anu",24)
pe1.printvalue()

pe2=Person()
pe2.setvalue("saji",33)
pe2.printvalue()