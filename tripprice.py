def hotel(nights) :
    return 140 * nights

def plane(city) :
    if "Melbourne" == city :
        return 183 
    elif "Sydeny" == city :
        return 220
    elif "adelaide" == city :
        return 222
    elif "LosAngeles" == city :
        return 475
    
def rentalcar(days) :
    if days >= 7 :
        return 40 * days - 50
    
    elif days >= 3 :
        return 40 * days - 20
    
    else :
        return 40 * days
    
def tripcost(city,days,spendingmoney) :
    return rentalcar(days)+hotel(days) + plane(city) + spendingmoney 

print("cost of car rental " , rentalcar(5))

print("cost of plane ticket",plane("Sydeny")) 

print("cost of hotel room",hotel(7)) 

print("total cost of the trip ",tripcost("Sydeny",7,1000))