class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Bus(Vehicle):
    def __init__(self, name, price, fare):
        super().__init__(name, price)
        self.fare = fare

    def total_fare(self):
        return self.fare + (self.fare * 0.10)

    def display(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Normal Fare:", self.fare)
        print("Fare with 10% extra:", self.total_fare())


school_bus = Bus("Tata", 500000, 100)

school_bus.display()