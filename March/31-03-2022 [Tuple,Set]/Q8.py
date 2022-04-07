a , b , c= (1,2,3,4), (3,5,2,1), (2,2,3,1)
sum_list = []
for i in range(4):
    sum_list.append(a[i]+b[i]+c[i])
sum_tuple = tuple(sum_list)
print(sum_tuple)