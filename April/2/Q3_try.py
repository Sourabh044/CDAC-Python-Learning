d = {'Ram' : '15/07/1989','Krishna': '09/12/1968','Venkat': '11/02/2006'}
Date = input('Enter DOB in dd/mm/yyyy: ')
date = Date.split(sep="-")
date_str = date[0]+'/'+ date[1]+"/"+date[2]
f = 0
for i in d:
    if date_str == d[i]:
        print('Name:',i)
        f +=1
        break
if f==0:
    print('Not Found..!')