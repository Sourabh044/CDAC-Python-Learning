''' Age Calculator'''
from datetime import datetime
import math
import os
os.system('cls')
user_date = input('Enter date in dd-mm-yyyy: ')
date = datetime.strptime(user_date,'%d-%m-%Y')
x = datetime.now()
# print(x)
y = x-date
days = str(y.days/365).split('.')
days[1] = '0.'+ days[1]
months = float(days[1])*12
# print(days)
print('Your current age is',math.floor(y.days/365), 'Years', 'and',math.floor(months),'Months.')
# os.system('exit')