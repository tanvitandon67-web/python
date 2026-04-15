try :
    num = int(input("enter your age = "))
    if num % 2 == 0 :
        print ("even")
    
    else : 
        print ("odd")

except ValueError as ex :
    print("YOU HAVE NOT FOLLOWED THE INSTRUCTIONS.PLEASE MAKE IT AS AN INTEGER NOT DECIMAL OR WORDS")
    


