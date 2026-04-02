def add (a,b) :
    return a + b

def sub (a,b) :
    return a - b

def muti (a,b) :
    return a * b

def divi (a,b):
    return a / b

print ("please select the following options ")
print("a.  Addition")
print("b.  Subtraction")
print("c.  Mutiplcation")
print("d.  Divison")

choice = input("please enter your choice a/b/c/d : ")

num1 = int(input("please enter your first number :"))
num2 = int(input("please enter your 2nd number :"))

if choice == "a" :
    print( add(num1,num2))

elif choice == "b" :
    print(sub(num1,num2))

elif choice == "c" :
    print(muti(num1,num2))

elif choice == "d" :
    print(divi(num1,num2))
else:
    print("this is invaild input ")

