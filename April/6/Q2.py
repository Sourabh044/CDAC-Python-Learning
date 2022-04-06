class student:
    def __init__(self):
        self.sid = ''
        self.name = ''
        self.marks = []
        self.subjects = ['C','Python','C++','Django','HTML']    
    def inputDetails(self):
        print('Enter details')
        self.name = input('Enter the Name of the Student: ')
        self.sid = int(input('Enter the sid: '))
        print('------Enter Marks in 5 Subjects One by One------'.center(50))
        for i in self.subjects:
            print('Enter marks of subject',i,':',end=' ')
            a = int(input())
            self.marks.append(a)
            print('------'.rjust(20))
    
    def showdetails(self):
        print('Details of',self.name)
        print('Name = ',self.name)
        print('Student id = ',self.sid)
        print('Marks list = ',self.marks)

    def totalMarks(self):
        print('Totals Marks of the student is:',sum(self.marks))
    def displayGrade(self):
        total = sum(self.marks)
        if total<500 and total>450:
            print('Grade A')
        elif total<450 and total>350:
            print('Grade B')
        elif total<350 and total>200:
            print('Grade C')
        elif total<200:
            print('Grade D')

# Creating Student object
s1 = student()
s1.inputDetails()
print('---------------------------')
s1.showdetails()
print('---------------------------')
s1.totalMarks()
s1.displayGrade()
# Creating another student object
s2 = student()
s2.inputDetails()
print('---------------------------')
s2.showdetails()
print('---------------------------')
s2.totalMarks()
s2.displayGrade()