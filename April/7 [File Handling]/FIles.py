try:
    f = open('a.txt',"w+")
    f.write('Hello Bro')
    f.seek(0)
    print(f.read())
    f.close()
    print(f.closed)
except:
    print('File Not found')
    print('Creating new file')
    f = open('a.txt','w')
    f.write('New file')
    f.close()