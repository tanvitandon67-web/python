word =  input("please enter your word = ")
char  =  input("please enter the  charcter you want to know its occuarnce  = ")
i = 0
count = 0
while (i < len(word)) :
    if word [i] == char:
        count = count + 1
    i = i + 1
print("the total number of times the charcter occured",count)     
