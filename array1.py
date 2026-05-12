import array as arr

array_number = arr.array('i',[1,3,5,3,7,9,3,])
print("original arry is = " +str(array_number))

print("number of occurence of 3 in array = " +str(array_number.count(3)))

array_number.reverse()
print(str(array_number))