class Student:
    def setvalue(self,studentname,rollno,department,collegename):
        self.studentname=studentname
        self.rollno=rollno
        self.department=department
        self.collegename=collegename
    def printvalue(self):
        print(self.studentname,self.rollno,self.department,self.collegename)
st1=Student()
st1.setvalue("ammu",1,"science","sngc")
st1.printvalue()



#instance variable....related to method...access using self
#static variable.....related to class...access using class name