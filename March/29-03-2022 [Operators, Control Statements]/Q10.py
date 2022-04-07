# Taking 3 numbers from the user
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if (a>b): 
    if(a<c):
        print(c,'is Greater')
    else:
        print(a,'is Greater')
if(b>a):
    if(b>c):
        print(b,'is Greater')
    else:
        print(c,'is Greater')