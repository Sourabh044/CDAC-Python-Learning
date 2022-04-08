f = open('Q3.txt','w+')
# Taking fruit names
fruits = []
print('Enter 10 Fruits names')
for i in range(10):
        fruits.append(input('Enter fruit name:'))
        fruits.append('\n')
f.writelines(fruits)
f.seek(0)
print(f.read())
f.close()
