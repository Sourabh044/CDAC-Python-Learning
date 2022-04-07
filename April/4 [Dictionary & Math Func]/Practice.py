students = {1:{'Name': 'Sourabh', 'Phone_No': 8351943455, 'Address': 'Karampur'}, 
            2:{'Name': 'Kunal', 'Phone_No': 1010018825, 'Address':'Kharar'},
            3:{'Name': 'Ayaan', 'Phone_No': 9810100188, 'Address':'Mohali'}}

print('------------------')
print("First Method")
print('------------------')
for a in students:
    for k,v in students[a].items():
        print(k,v) 
print('------------------')
print('Second Method')
print('------------------')
for k,v in students.items():
    for a in v:
        print(a,students[k][a])
    print('-------')


