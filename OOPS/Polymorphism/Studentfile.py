class Student:
    college_name="luminar"
    def setval(self,name,rollno,dep):
        self.name = name
        self.rollno = rollno
        self.dep=dep

    def printstud(self):
        print(self.name, self.rollno,self.dep,Student.college_name)
f=open("student", 'r')
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    roll=data[1]
    dep=data[2]
    st=Student()
    st.setval(name,roll,dep)
    st.printstud()
