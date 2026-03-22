n = int(input("enter a number to count the digits = "))
count  = 0
if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count = count + 1
print("total number of digit =", count)




