import random
f = open('num.txt','w+')
# Taking rand nums
rand_nums = [random.randint(1,501) for x in range(5)]
# Writing number in file
for i in rand_nums:
    f.write(str(i))
    f.write('\n')




