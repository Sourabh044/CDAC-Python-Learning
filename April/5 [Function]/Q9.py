def SumAll(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
print('sum',SumAll(5,9,6))

def Greet(*names):
    for name in names:
        print('Hello',name)
Greet('Sourabh','Suraj','Himanshu')
