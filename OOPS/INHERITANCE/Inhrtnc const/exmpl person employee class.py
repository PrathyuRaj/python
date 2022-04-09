class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,id,department,dob,name,age):
        super().__init__(name,age)
        self.id=id
        self.department=department
        self.dob=dob
    def printst(self):
        print(self.name,self.age,self.id,self.department,self.dob)
st=Student(122,"cse",12021,"kloki",20)
st.printst()