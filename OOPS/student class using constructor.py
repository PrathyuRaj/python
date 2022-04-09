class Student:
    def __init__(self,studentname,rollno,department,collegename):
        self.studentname=studentname
        self.rollno=rollno
        self.department=department
        self.collegename=collegename
    def printvalue(self):
        print(self.studentname,self.rollno,self.department,self.collegename)
st1=Student("anu",1,"sci","lumi")
st1.printvalue()
st=Student("kiran",121,"maths","ajk")
st.printvalue()