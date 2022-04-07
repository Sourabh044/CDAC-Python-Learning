name = input('Enter Your Full Name: ') #'Sourabh Kumar'
name_split = name.split()
age = 21
nameFirstChar = [name_split[0][0].lower(),name_split[1][0].lower()]

nameMidvalue = [name[int(len(name_split[0])/2)] ,name[int(len(name_split[1])/2)]]
print('passwords are ',nameFirstChar[0]+nameFirstChar[1],age,' and ',nameMidvalue[0]+nameMidvalue[1],age*2,sep='')