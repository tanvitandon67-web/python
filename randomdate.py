import random
import time
def getrandomdate(startdate,enddate) :

    print("printing random date between " , startdate, "and", enddate) 
    randomGenerator = random.random()
    dateFormat = "%m/%d/%y"
    starttime= time.mktime(time.strptime(startdate,dateFormat))
    endtime= time.mktime(time.strptime(enddate,dateFormat))

    randomtime = starttime + randomGenerator * (endtime - starttime )
    randomdate = time.strftime(dateFormat,time.localtime(randomtime))
    return randomdate 
print("randomdate =" ,getrandomdate("5/27/25","4/27/26"))


