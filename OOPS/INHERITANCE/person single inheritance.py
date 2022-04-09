class Person:
    def setp(self,name,age):
        self.name=name
        self.age=age
    def printp(self):
        print("is",self.name,self.age)
class Student(Person):
    def sets(self,rollno,dep):
        self.rollno=rollno
        self.dep=dep
    def prints(self):
        print(self.rollno)
        print(self.dep)
        print(self.name,self.age)
st=Student()
st.setp("sarath",12)
st.printp()







class Employee(Person):
    def sete(self,name,id,desig,salary):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
    def printe(self):
        print(self.name,self.id,self.desig,self.salary)
        print(self.name,self.age)
emp=Employee()
emp.setp("anu",20,)
emp.sete(1,20,10,1000)
emp.printe()