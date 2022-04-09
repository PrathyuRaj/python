class Student:
    college_name="luminar"
    def setvalue(self,studentname,rollno,department,):
        self.studentname=studentname
        self.rollno=rollno
        self.department=department
    def printvalue(self):
        print(self.studentname, self.rollno, self.department,Student.college_name)
st1 = Student()
st1.setvalue("ammu", 1, "science")
st1.printvalue()