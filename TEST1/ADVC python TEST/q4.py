class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name,self.age)
class Dog(Animal):
    def __init__(self,breed,vaccinateddate,name,age):
        super().__init__(name,age)
        self.breed=breed
        self.vaccinateddate=vaccinateddate
    def printst(self):
        print(self.name,self.age,self.breed,self.vaccinateddate)
an=Dog("shitzu","12/april/21","whiskey",4)
an.printst()
