person_info = {}
for i in range(1,3):
    Single_person = {}
    Single_person['First_Name'] = input('Enter  First Name: ')
    Single_person['Last_name'] = input('Enter Last Name: ')
    Single_person['Age'] = int(input('Enter Age: '))
    Single_person['City'] = input('Enter City: ')
    person_info[i] = Single_person
print("---Printing the Details---".center(50))
for i in person_info:
    for k,v in person_info[i].items():
        print(k,v)
    print('------------')