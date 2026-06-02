class Computer :

    def __init__(self):
        self.__maxprice = 900

    def sell(self) :
        print("Selling price : {}".format(self.__maxprice))

    def setmaxpice(self,price) :
        self.__maxprice = price


ob1 = Computer()
ob1.sell()

ob1.__maxprice = 1000
ob1.sell()

ob1.setmaxpice(1000)
ob1.sell()







    