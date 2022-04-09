class Vehicle:
    def setvh(self,reg,model,color):
        self.reg=reg
        self.model=model
        self.color=color

    def printvh(self):
        print(self.reg,self.model,self.color)

class Bus(Vehicle):
    def setbus(self,capacity):
        self.capacity=capacity

    def printbus(self):
        print(self.reg,self.model,self.color,self.capacity)

bus1=Bus()
bus1.setvh('KL',2019,"red")
bus1.setbus('45 seater')
bus1.printbus()