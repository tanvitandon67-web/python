num = int(input("enter a number = "))
t = num
numlength = 0
while (t > 0) :
    numlength = numlength + 1
    t = int (t / 10)
if numlength >= 4:
    numlength = int (numlength/2) 
    chk = 0 
    while num > 0 :
        rem = num % 10
        if chk == (numlength ) :
            mid1 = rem 
        elif chk == numlength - 1 :
            mid2 = rem
        num = int(num/ 10)
        chk = chk + 1
    prod = mid1 * mid2 
    print("product of 2 main numbers =",prod)




