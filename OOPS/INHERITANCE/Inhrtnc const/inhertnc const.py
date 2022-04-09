class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,roll,dep,name,age):
        super().__init__(name,age)  #superfunction functionname called,no self,no colun
        self.roll=roll
        self.dep=dep
    def printst(self):
        print(self.name,self.age,self.roll,self.dep)
st=Student(1,"cse","anu",12)
st.printst()