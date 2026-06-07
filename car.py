class BMW():
    def fuel(self) :
        print("The fuel type is Unleaded")

    def maxspeed (self) :
        print("The max speed is 300km ")



class Ferrari():
    def fuel(self) :
        print("The fuel type is Unleaded")

    def maxspeed(self) :
        print("The max speed is 250km")

 

ob1 = BMW()
ob2 = Ferrari()

for i in (ob1,ob2) :
    i.fuel()
    i.maxspeed()
   
