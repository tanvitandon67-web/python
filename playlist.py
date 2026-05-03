lst = [4,5,1,2,9,7,10,8]
print("original list is",lst)

count = 0

for i in lst :
    count = count + i

average  = count / len(lst)
print("Sum is =",count )
print("average = ",average)

lst.sort()
print("smallest element of list = ",lst[0])
print(" largest element of list = ",lst[-1])

