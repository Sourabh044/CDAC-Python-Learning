temp = (36.5,37,37.5,39)
print('Original List:',temp)
print('------------------'.center(50))
# fahrenheit to celcius
celcius_list = list(map(lambda x:(x-32)*5/9,temp))
print('Printing the Celcius list',celcius_list)
print('---------------------------------------------------------------'.rjust(90))
#  celcius to fahrenheit
fahrenheit_list = list(map(lambda x:(x*1.8)+32,celcius_list))
print('Printing the Fahrenheit list',fahrenheit_list)
print('---------------------'.rjust(50))