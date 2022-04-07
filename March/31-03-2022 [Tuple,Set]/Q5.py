x = [(10,20,30),(40,50,60),(70,80,90)]
print("memory location before",id(x))
rep = int(input('Enter a number: '))
print('Before replacing Value',x)
i = 0
for tup in x:
    list_tup = list(tup)
    list_tup[2] = rep
    tup = tuple(list_tup)
    x.pop(i)
    x.insert(i,tup)
    i +=1
print("memory location after",id(x))
print('After replacing Value',x)
