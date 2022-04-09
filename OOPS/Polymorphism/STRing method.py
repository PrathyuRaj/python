# to convert to str methiod    [to string method]
class Student:
    def __init__(self,studentname,rollno,department):
        self.studentname=studentname
        self.rollno=rollno
        self.department=department
        # self.collegename=collegename
    def printvalue(self):
        print(self.studentname,self.rollno,self.department)
    def __str__(self):
        return self.studentname+self.department+str(self.rollno)
st1=Student("anu",1,"sci")
st2=Student("kiran",121,"maths")
print(st1,st2)