rowsize = int(input("enter the amount of rows = "))
if rowsize % 2 == 0 :
    halfdimond = int(rowsize/2)
else :
    halfdimond = int(rowsize/2) + 1

space = halfdimond - 1
for i in range(1,halfdimond + 1) :
    for j in range (1,space + 1) :
        print(end = " ")
    space = space - 1
    num = 1
    for j in range(2 * i - 1) :
        print(end = str(num))
        num = num + 1
    print ()
space = 1
for i in range (1,halfdimond) :
    for j in range(1,space + 1) :
        print(end = " ")
    space = space + 1
    num = 1
    for j in range(1,2 *(halfdimond - i)) :
        print( end = str(num))
        num = num + 1
    print ()


