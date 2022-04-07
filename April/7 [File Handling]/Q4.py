with open('Q4.txt') as a:
    s = a.readlines()
    print('Student Details before sorting')
    for i in s:
        print(i)
s.sort()
f = open('Q4.txt','w+')
f.writelines(s)
print('Student Details After sorting:')
f.seek(0)
for i in f:
    print(i)
f.write(' \n')
f.close()
