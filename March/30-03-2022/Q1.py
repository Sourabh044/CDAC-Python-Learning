numbers = [1,3,5,7,9,11,13,15,2,4,6,8,10,12,14,16]
x = int(input("Enter the element: "))
if x in numbers:
    print('Index is',numbers.index(x))
else:
    print('Not Found')