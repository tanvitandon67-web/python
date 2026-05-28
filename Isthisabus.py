class vehicle : 
    def __init__(self,name,maxium,mileage):
        self.name = name
        self.maxium = maxium
        self.mileage = mileage


class bus(vehicle):
    pass

school_bus = bus("tata",240,20)

print(school_bus.name)
print(school_bus.maxium)
print(school_bus.mileage)

        