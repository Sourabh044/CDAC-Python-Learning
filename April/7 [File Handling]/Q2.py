f = open("Q2.txt",'r')
word = []
print('Total Number of lines in Q2.txt:',len(f.readlines()))
f.seek(0)
spaces = list(map(lambda a:a==' ',f.readlines()))
f.seek(0)
print('total characters in the list',len(f.read())-(len(spaces)+len(f.readlines()) ) )
f.seek(0)
for i in f:
    word.extend(i.split())
print('Total Word in the list is:',len(word))
f.close()