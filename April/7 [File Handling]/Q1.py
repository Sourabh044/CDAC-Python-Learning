f = open('Q1.txt','r')
rev = []
for i in f: #Traverisng file
    a = list(reversed(i)) #reversing each word
    rev.append(a)
for i in rev:
    for word in i:
        print(word,end='')
print('')
f.close()