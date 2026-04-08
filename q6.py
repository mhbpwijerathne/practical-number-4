
gpa = float(input("Enter gpa"))
income = float (input("Enter income"))

if gpa >= 3.5 and income < 30000 :
    print ("full scholarship")
    
elif gpa >= 3.0 and income < 50000 :
    print ("partial scholarship")

else :
     print ("no scholarship")

