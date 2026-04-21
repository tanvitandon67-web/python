import random 
while True :
    user_action = input("enter a choice between rock,paper,scissor")
    possible_actions = ["rock","paper","scissor"]
    computer_action = random.choice (possible_actions )
    print(f"\n you have chosen{user_action},computer has chosen{computer_action}")

    if user_action == computer_action:
        print('its a tie!')

    elif user_action == "rock" :
        if computer_action == "scissor":
            print("YOU WIN")
        else :
            print("you lose")
    
    elif user_action == "paper" :
        if computer_action == "rock":
            print("YOU WIN")
        else :
            print("you lose")

    elif user_action == "scissor" :
        if computer_action == "paper":
            print("YOU WIN")
        else :
            print("you lose")

    play_again = input("do you want to play again?? y/n")
    if play_again != "y" :
         break
    
 
        


        
        



    


