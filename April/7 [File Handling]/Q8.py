with open('num.txt') as f:
    s  = f.readlines()
sum = 0
for i in s:
    num = i.split('\n')
    sum += int(num[0])
print('The sum of the number in the num.txt file is:',sum)