import math
# Taking A cordinates
print('Enter Value of A cordinates')
x1 = float(input("Enter Value: "))
y1 = float(input("Enter Value: "))
a_coordinates = (x1,y1)
print('A',a_coordinates,sep='')
# Taking B cordinates
print('Enter Value of A cordinates')
x2 = float(input("Enter Value: "))
y2 = float(input("Enter Value: "))
b_coordinates = (x2,y2)
print('B',b_coordinates,sep='')
# calculating distance using 
AB = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
print(AB)