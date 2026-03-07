user_input = input("Enter a character: ")

if type(user_input) == str and len(user_input) == 1:
    ascii_value = ord(user_input)
    print("ASCII value of", user_input, "is", ascii_value)

elif type(user_input) == str and len(user_input) > 1:
    print("Please enter only ONE character.")

else:
    print("Invalid input.")