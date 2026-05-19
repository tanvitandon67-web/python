# results
grade = {"emma": 90,"Sam": 78,"Charlie" : 45, "Alice" : 94, "Harry" : 80}
mark = grade.values()
print ("student results")
for name in grade :
    print(name,grade[name])

# average
average = sum(mark) / len(grade)
print("The class average is ",average)


# top grade
max1 = max(grade,key = grade.get)
print(max1)

# lowes grade
min1 = min(grade,key=grade.get)
print(min1)

# grade search
search = str(input("Enter a student name that did the test to see there results = "))
name = grade.get(search)
print(name)

