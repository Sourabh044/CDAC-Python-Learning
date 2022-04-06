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
    result = 'Remainder on dividing '+ str(num1) + ' and ' + str(num2) + ' is ' + str(num1 % num2) 
    return result 
def proDuct(num1,num2):
    result = 'Product of '+ str(num1) + ' and ' + str(num2) + ' we get ' + str(num1 * num2) 
    return result 
def power(num1,num2):
    result = 'Raising power of '+ str(num1) + ' by ' + str(num2) + ' we get ' + str(num1**num2) 
    return result
print('-----------------------------------------------'.center(50))
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
print('-----------------------------------------------'.center(50))
print(add(a,b))
print('-----------------------------------------------'.center(50))
print(sub(a,b))
print('-----------------------------------------------'.center(50))
print(div(a,b))
print('-----------------------------------------------'.center(50))        
print(mod(a,b))
print('-----------------------------------------------'.center(50))        
print(proDuct(a,b))
print('-----------------------------------------------'.center(50))        
print(power(a,b))