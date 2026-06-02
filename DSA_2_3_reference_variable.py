class customer:
    def __init__(self, name):
        self.name = name





# ----------------------------------------------------

cust = customer('jeet')

print(cust.name)



def greet(obj):
    print(f"Hello {obj.name}")

greet(cust)











