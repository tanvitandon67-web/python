print("the mean value of 40 numbers is 38,later on I detected that I miss read the number 56 as 36 find the correct mean")
mean1 = 38
wrong = 36
correct = 56
total = 40
sum = mean1 * total 
print("sum of 40 numbers is equal to",sum)
number2 = sum - (wrong - correct )
print("sum after correction = ", number2)
mean2 = number2 / total
print("the corrected mean is = ",mean2)