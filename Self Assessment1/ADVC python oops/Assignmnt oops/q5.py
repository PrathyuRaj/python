#creating objects for the following employees
class Employee:
    def setvalue(self,name,id,position,salary):
        self.name=name
        self.id=id=id
        self.position=position
        self.salary=salary
    def printvalue(self):
        print(self.name,self.id,self.position,self.salary)
emp=Employee()
emp.setvalue("Arun",1,"Devoloper",45000)
emp.printvalue()

emp1=Employee()
emp1.setvalue("Amal",2,"Tester",34000)
emp1.printvalue()

emp2=Employee()
emp2.setvalue("Alan",3,"Developer",50000)
emp2.printvalue()

emp3=Employee()
emp3.setvalue("Anagha",4,"Tester",30000)
emp3.printvalue()

emp4=Employee()
emp4.setvalue("Maya",5,"Developer",67000)
emp4.printvalue()

