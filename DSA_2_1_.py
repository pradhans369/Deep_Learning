class a:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    

    def show(self):
        return self.__name, self.age
    


b = a('ashura', 55)

print(b.show())
# print(b.__name)
print(b._a__name)       # this is how you print private variables
print(b.age)

b.area = 'Kanpur'       # this here created a new variable
print(b.area)

