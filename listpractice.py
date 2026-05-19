numbers = input("Enter some numbers = ").split()

odd = [1, 3, 5, 7, 9]

odds = list(zip(numbers, odd))

odd_numbers = [num for num, value in odds if value % 2 != 0]

print("List of odd numbers:", odd_numbers)




fruits = ["apple", "banana", "cherry", "orange", "grapes"]

capital_fruits = [fruit.upper() for fruit in fruits]


print("Original List:", fruits)
print("Capital Letters List:", capital_fruits)