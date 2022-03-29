# (i)
columns = int(input('Enter the number of colums'))
temp = columns
while(columns!=0):
    for i in range(5):
        print('*\t*\t*\t*')
        columns -= 1
print('\n')
# (ii)
columns = temp #int(input('Enter the number of colums'))
for i in range(columns+1):
    for j in range(i+1):
        print('*', end=" ")
    print('\n')
print('\n')

# (iii)
for i in range(columns+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print('\n')
print('\n')

# (iv)
x = 1
for i in range(1,columns+1):
    for j in range(1,i+1):
        print(x, end=' ')
        x += 1
    print('\n')


