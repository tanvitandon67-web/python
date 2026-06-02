class myClass :
    __privateVar = 27
    def __privmeth(self):
        print("I am inside my class")

    def hello(self) :
        print("Private varible = ",myClass.__privateVar)



ob1 = myClass()
ob1.hello()
ob1.__privmeth()
