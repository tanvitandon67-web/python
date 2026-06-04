from abc import ABC, abstractmethod 


class abs(ABC):

    def print(self,x) :
        print("The value is = ",x)


    def task(self) :
        print("We are inside abstract task")


class test_class(abs) :
    def task(self) :
        print("We are inside the subclass task ")


test = test_class()
test.task()
test.print(100)