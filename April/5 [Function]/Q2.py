def cube(num):
    return num**3
def sq(num):
    return num**2

s = lambda a: a**2
c = lambda a: a**3
num = int(input('Enter a Number : '))
print('Square by function :',sq(num))
print('Square by lamda function :',s(num))
print('Cube by function :',cube(num))
print('Cube by lamda function :',c(num))