try :
    num1,num2= eval(input("enter your 2 numbers seperated with comma = "))
    result = num1 / num2
    print("result = ",result )
except  ZeroDivisionError :
    print("THE DIVISION BY ZERO HAS CAUSED AN ERROR ")

except SyntaxError :
    print("YOU HAVE FORGOTTEN THE COMMA ")

except :
    print("WRONG INPUT :( ")

else :
    print("no exception :) ")

finally :
    print("THIS WILL BE HERE NO MATTER WHAT YOU DO")

