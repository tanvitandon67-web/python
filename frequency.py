test_dict1 = {'codingal' : 2,'is' : 2, 'the' : 2 , 'best' : 9999999}
print("The original dictonary :" +str(test_dict1) )

oc = 2
tot = 0
for key in test_dict1 :
    if test_dict1[key] == oc :
        tot = tot + 1


print("The frequerncy of 2 is : " +str(tot))