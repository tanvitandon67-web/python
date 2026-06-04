class India():
    def capital(self) :
        print("New Dehli is the capital of india")

    def language (self) :
        print("Hindi is the mose widely spoken languge spoken in india")

    def Type(self) :
        print("India is a developing country ")


class Australia():
    def capital(self) :
        print("ACT is the capital of Australia")

    def language (self) :
        print("English is the mose widely spoken languge spoken in Australia ")

    def Type(self) :
        print("Australia is a developing country ")

ob1 = India()
ob2 = Australia()

for i in (ob1,ob2) :
    i.capital()
    i.language()
    i.Type()
