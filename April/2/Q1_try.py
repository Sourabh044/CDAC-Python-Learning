person_info = {}
for i in range(1,3):
    # Single_person = {}
    # Single_person['First_Name'] = input('Enter  First Name: ')
    # Single_person['Last_name'] = input('Enter Last Name: ')
    # Single_person['Age'] = int(input('Enter Age: '))
    # Single_person['City'] = input('Enter City: ')
    name = input('Enter  First Name: ')
    last_name = input('Enter Last Name: ')
    Age = int(input('Enter Age'))
    city = input('Enter City: ')
    person_info[i] = {'First_Name': name, 'Last_name': last_name, 'Age': Age, "City": city}
    # person_info = person_info | Single_person
    # person_info.extend(Single_person) #= Single_person

print(person_info)
exit()
for i in person_info:
    for k,v in person_info[i].items():
        print(k,v)
    print('------------')
    # Error in this