import random 
play = True
num = str(random.randint(0,9))
print("I will generate a number from zero to nine.You have to guess the number once at a time.Good luck!")
while play :
    guess = input("give me your best guess")
    if num == guess :
        print("YOU WIN!!!")
        print("The number was",num)
        break
    else :
        print("your guess is not right try again")

        