while(columns!=0):
for i in range(columns+1):
    for j in range(i+1):
        print('*', end=" ")
    print('\n')
for i in range(columns+1):
    for j in range(1, i):
        print(j, end=" ")
    print('\n')
