n = int(input("enter your number to check ="))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10
if n == sum :
    print("number is armstrong number")
else :
    print("number is not armstrong number")
