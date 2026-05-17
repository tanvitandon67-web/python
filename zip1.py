s1 = {1,2,3}
s2 = {'a','b','c'}
s3 = list(zip(s1,s2))

print(s3)

list1 = [10,20,30,40]
list2 = [100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

stock = ['reliense','infosys','TCS']
prices = [2175,1127,2750]

my_dic = {stock : prices for stock,prices in zip(stock,prices)}
print(my_dic)

