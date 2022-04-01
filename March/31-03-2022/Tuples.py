Details = ('Name', 'Age', 'Phone No.')
student_list = []
number = int(input('Kitna Bhai '))
for i in range(number):
    y = 0
    for x in range(number):
        single = []
        name = input('Enter {} '.format(Details[y]))
        single.append(name)
        roll_no = input('Enter {} '.format(Details[y+1]))
        single.append(roll_no)
        Phone_no = input('Enter {} '.format(Details[y+2]))
        single.append(Phone_no)
        student_list.append(single)

print(student_list)

# Tuple Table
n = int(input("Enter the Number: "))
till = int(input("Untill Tbale required: "))
n = 5
t = tuple([i for i in range(n,n*11,n)])
print(t)
