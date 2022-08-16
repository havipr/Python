mark = float(input("How many marks: "))
if(mark >= 85):
    print("Grade awarded: 7")
elif(75 <= mark < 85):
    print("grade awarded: 6")
elif(75 <= mark < 75):
    print("grade awarded: 5")
elif(50 <= mark < 65):
    print("grade awarded: 4")
elif(mark<50):
    print("Grade awarded: F")
else:
    print("Please insert a value number")