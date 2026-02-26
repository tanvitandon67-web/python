bp = int(input("enter the buying price = "))
sp = int(input("enter your selling price = "))
profit = sp - bp
loss = bp - sp
if (bp < sp ) :
    print("you are in profit")
    print("profit = ",profit )
else :
    print('you are in loss')  
    print("loss = " , loss)  


    