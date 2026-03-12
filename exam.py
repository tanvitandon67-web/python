medical_cause = input("did you have a medical cause Y/N")
if medical_cause == "Y" :
    print("you are allowed")
else:
     attendence = int(input("enter the attendence of the student = "))
     if attendence >= 75 :
          print("you are allowed")
     else:
          print("you are not allowed")