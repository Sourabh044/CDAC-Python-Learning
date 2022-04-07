with open('Q6.txt') as f:
    print('----------Before----------'.center(50))
    for i in f:
        print(i)
    print('----------After----------'.center(50))
    f.seek(0)
    for i in f:
        print(i.upper())
