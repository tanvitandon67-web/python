class Dog:
    species = 'Dog'
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        

ob1 = Dog("Oreo","Golden retriver")
ob2 = Dog("Maggi","Poodle")


print("{} is a {} type ".format(ob1.name,ob1.breed))
print("{} is a {} type ".format(ob2.name,ob2.breed))

