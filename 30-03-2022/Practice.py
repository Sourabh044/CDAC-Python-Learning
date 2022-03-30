# Take a student name and then its marks save it in a list
# then insert it in a list and create a list of students
# Basically, it will be a list of students, where the elements will be details of a single student.
# Also sort the list

studentDetails = []
totalStudents = int(input('Enter the total number of students: '))

for i in range(totalStudents):
    print('Enter the details of',i+1,'Student')
    singleStudent = []
    Name = input('Enter name: ')
    singleStudent.append(Name)
    Roll_number = int(input('Enter Roll Number: '))
    singleStudent.append(Roll_number)
    Phone_number = int(input('Enter Phone Number: '))
    singleStudent.append(Phone_number)
    studentDetails.append(singleStudent)
    studentDetails.sort()

# print(studentDetails)
for student in studentDetails:
    y = 0
    for details in student:
        d = ['Name:','Roll No:','Phone Number:']
        # for i in d:
        print(d[y],details, end=" ")
        y += 1
    print('--------------------------------------------------------------------------------\n')