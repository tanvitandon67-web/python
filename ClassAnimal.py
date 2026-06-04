from abc import ABC, abstractmethod 

class Animal(ABC) :

    def move(self) :
        pass


class Human(Animal) :

    def move(self):
        print("I CAN WALK AND RUN")
       

class Snake(Animal) :
    
    def move(self):
        print("I CAN CRAWL")


class Dog(Animal) :
    
    def move(self):
        print("I CAN BARK")

class  Lion(Animal) :
    
    def move(self):
        print("I CAN ROAR")

r = Human()
r.move()

k = Snake()
k .move()

m = Dog()
m.move()

l = Lion()
l.move()





