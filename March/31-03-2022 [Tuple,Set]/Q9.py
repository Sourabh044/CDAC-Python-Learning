x = [(1,2),(2,3,5),(3,4),(2,3,4,2)]
i = 0
for tup in x:
    list_tup = list(tup)
    x.pop(i)
    x.insert(i,list_tup)
    i += 1
print(x)