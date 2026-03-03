w = float(input("enter your weight  in killograms = "))
h = float(input("enter your height in centermeteres = "))
bmi = w / ( h / 100)**2
print ("your Bmi is = ", bmi)
if bmi <= 18.4 :
    print("you are under weight")
elif bmi<= 24.9 :
    print("you are healthy")   
elif bmi <= 29.9 :
    print(" you are over weight ")    
elif bmi <= 34.9 :
    print ("you are severly over weight")  
else :
    print (" you are swerly obeice")   


