print("Write a code to check the given tuple if palindrone or not")

def palin(r) :
    e = len(r)-1
    s = 0
    while s < e :
        if (r[s] != r[e]) :
            return False
        
        s = s + 1 
        e = e - 1
    return True

r = (1,2,3,3,2,1)

if(palin(r)) :
    print("The tuple if flipflop")

else :
    print("the tuple is not flipflop")