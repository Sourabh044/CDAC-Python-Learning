while(True):
 print("-------------------------------------------------------------------------------------------------------------------------")   
 print('Menu: \n1. Addition\n2. Subtraction\n3. Mulpication\n4. Division(float)\n5. Division(integer)\n6. Exponent\n')
 x = int(input('Enter Your Choice: '))
 if(x<6):
    a = int(input('Enter First Number : '))
    b = int(input('Enter Second Number : '))
    if(x==1):
        print("sum = ",a+b)
    elif(x==2):
        print("Difference = ",a-b)
    elif(x==3):
        print('Product = ',a*b)
    elif(x==4):
        print('Qoutient = ',a/b)
    elif(x==5):
        print('Qoutient = ',a//b)
 else:
    a = int(input('Enter the Number:\t'))
    b = int(input('Enter the Exponential Value: \t'))
    print(a**b)
        
# Operators
