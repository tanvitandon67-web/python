class Parrot :
    species = 'Bird'
    def __init__(self,name,age):
        self.name = name
        self.age = age
        

ob1 = Parrot("Blu",10)
ob2 = Parrot("Woo",12)


print("{} is {} years old ".format(ob1.name,ob1.age))
print("{} is {} years old ".format(ob2.name,ob2.age))

