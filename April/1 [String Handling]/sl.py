'''s = set()
l = []
for i in range(2):
    s.add(input('Enter Number ; '))
    l.append(input('Enter Character: '))
print(s,l,sep="\n")

for i in range(1,11):
    print(i)'''

import array as arr
a  = arr.array('i',[x for x in range(11) if x%2==0])
print(a)

while(True):
    choice = int(input('1. Add Element \n 2. Remove Element \n 3. Delete Array : '))

    if choice==1:
        e = int(input('Enter the Element to Insert: '))
        a.append(e)
    elif choice==2:
        print(a)
        e = int(input('Enter the Element you want to remove: '))
        a.remove(e)
        print(a)
        print('Item Removed')
    elif choice==3:
        e = input('Press y to delete array or any key to exit: ')
        if e=='y' or e=='Y':
            del a
            print('array Deleted')
            break 
