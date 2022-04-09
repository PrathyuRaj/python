class Person:
    def setp(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent(Person):
    def par(self,phn,address):
        self.phn=phn
        self.address=address
        print(self.phn,self.address)
class Employee(Person,Parent):
    def sete(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
        print(self.id, self.desig,self.salary,self.name,self.age,self.phn,self.address)

emp=Employee()
emp.setp("anu",23)
emp.par(123542415,"asdfds")
emp.sete(12,"bpo",120000)
emp.printe()