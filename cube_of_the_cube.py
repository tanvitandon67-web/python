def cube(num) :
    return num * num * num 

def div(num) :
    if num % 3 == 0 :
        return cube(num)
    else : 
        return False
    
print(div(3)) 
print(div(15))
