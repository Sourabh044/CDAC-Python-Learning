f = open('Q5-Details.txt','r')
username = input('Enter Username: ').title()
password = input('Enter Password: ')
s = f.readlines()
flag =0
password_correct = True

# print(s)
for i in s:
    if username in i:
            if password in i:
                print('* Your Login is Successfull *'.center(50))
                flag = 1
            else:
                print('Incorrect Password'.center(50))
                password_correct = False
if flag==0 and password_correct == True:
    print('XXXXXXXX This Username does not exist XXXXXXXX'.center(50))
f.close()