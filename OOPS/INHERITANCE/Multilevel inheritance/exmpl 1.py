class Person:
    def per(self,name,age):
        self.name=name
        self.age=age
        print("name is",self.name,"\n","age is",self.age)
class Child(Person):
    def setc(self,address,no):
        self.address=address
        self.no=no
        print("address is",self.address,"\n","num is",self.no)
class Student(Child):
    def setp(self,mark,dep):
        self.mark=mark
        self.dep=dep
        print("mark is",self.mark,"\n","dep is",self.dep)
p1=Student()
p1.per("saji",12)
p1.setc("abcs",985758596)
p1.setp(20,"science")