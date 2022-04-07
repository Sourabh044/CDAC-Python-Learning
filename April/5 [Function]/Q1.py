import os
# Creating the functions 
def add(num1,num2):
    result = 'Addition of '+ str(num1)  + ' and ' + str(num2) + ' is ' + str(num1 + num2) 
    return result
def sub(num1,num2):
    result = 'Difference of '+ str(num1) + ' and ' + str(num2) + ' is ' + str(num1 - num2) 
    return result
def div(num1,num2):
    result = 'Division of '+ str(num1) + ' and ' + str(num2) + ' is ' + str(num1 / num2) 
    return result
def mod(num1,num2):
    result = 'Modulus of '+ str(num1) + ' and ' + str(num2) + ' is ' + str(num1 % num2) 
    return result 
def exitt():
    print('Exiting Program......')
    return(exit())
# Creating endless loop
while(True):
    print('-----------------------------------------------'.center(50))
    choice = int(input('1. Add'+'|'.rjust(42) +'\n2. Subtract'+'|'.rjust(37) +'\n3. Division'+'|'.rjust(37) +'\n4. Modulus'+'|'.rjust(38) +'\n5. Exit'+'|'.rjust(41) +'\n'))
    print('-----------------------------------------------'.center(50))
    if choice == 1:
        os.system('cls')
        a = int(input('Enter number one: '))
        b = int(input('Enter number two: '))
        print('-----------------------------------------------'.center(50))
        print(add(a,b))
    elif choice == 2:
        a = int(input('Enter number one: '))
        b = int(input('Enter number two: '))
        print('-----------------------------------------------'.center(50))
        print(sub(a,b))
    elif choice == 3:
        a = int(input('Enter number one: '))
        b = int(input('Enter number two: '))
        print('-----------------------------------------------'.center(50))
        print(div(a,b))
    elif choice == 4:
        a = int(input('Enter number one: '))
        b = int(input('Enter number two: '))
        print('-----------------------------------------------'.center(50))        
        print(mod(a,b))
    elif choice == 5:
        # print('-----------------------------------------------'.center(50))
        exitt()
    else: 
        os.system('cls')
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'.center(50))        
        print('Enter Correct choice')    