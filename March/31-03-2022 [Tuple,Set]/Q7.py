fruits = (('mango', 'grapes', 'dragonfruit', 'water melon'), 
         ('kiwi', 'pomegranate','dates', 'papaya'),
         ('apple', 'banana', 'orange', 'litchi'))

fruit = input("Enter fruits: ")
x = 0
for flist in fruits:
    for i in flist:
        if(fruit==i):
            print('Available')
            x+=1
            break
if(x==0):
    print('Not Available')