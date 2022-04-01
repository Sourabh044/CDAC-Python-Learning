# Taking the Marks frm the user
Hindi = int(input('Enter Marks in Hindi Subject: '))
English = int(input('Enter Marks in English Subject: '))
Mathematics = int(input('Enter Marks in Maths Subject: '))
# Calculating Total and %age
Total = Hindi+English+Mathematics
Percentage = float(Total/300*100)
# Calculating Grade
if(Percentage<59):
    print("Grade is: D")
elif(Percentage>=60 and Percentage<=79):
    print("Grade is: C")
elif(Percentage>=80 and Percentage<=89):
    print("Grade is: B")
elif(Percentage>=90 and Percentage<=100):
    print("Grade is: A")