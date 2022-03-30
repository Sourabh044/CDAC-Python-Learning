# List demostration
totalStudents = int(input('Enter number of students: '))
Students = []
for i in range(totalStudents):
    x = input("Enter Name of the student: ")
    Students.append(x)

for i in Students:
    print(i)