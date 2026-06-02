class a:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def show(self):
        return self.name, self.age
    


b = a('ashura', 55)

print(b.show())
