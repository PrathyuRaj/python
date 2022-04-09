class Books:
    def pb(self,name):
        self.name=name
        print(self,name)

class Id(Books):
    def pb(self,id):
        self.id=id
        print("id of book is",self,id)
b1=Books()
b1.pb("abc")