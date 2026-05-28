class bird :
    def __init__(self):
        print("bird is ready")

    def whoisthis(self) :
        print("bird")


    def swim (self) :
        print("swim faster")


class penguin(bird) :
    def __init__(self):
        super().__init__()

    def whoisthis(self):
        print("penguin")


    def run(self):
        print("run faster")

ob1 = penguin()
ob1.whoisthis()
ob1.swim()
ob1.run()
