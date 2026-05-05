weather = (1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0)
print("rainy = 0,sunny = 1")
s = 0
r = 0

for i in range(0,22) :
    if (weather [i]== 0) :
       r = r + 1

    else :
        s = s + 1

if s > r :
    print("good weather")

else :
    print("bad weather be careful")