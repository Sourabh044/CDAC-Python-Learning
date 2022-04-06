import math
import random
# Creating list
n_list = [x for x in range(5,1001,5)]
op_list = [random.choice(n_list) for i in range(6)]
print(op_list)
print('maximum Number is ',max(op_list),'\n','Minimumber Number is ',min(op_list))
new_op_list = [random.choice(n_list) for i in range(6)]
print(new_op_list)
list3 = []
list3.append(pow(new_op_list[0],4))
list3.append(math.sqrt(new_op_list[1]))
list3.append(math.factorial(new_op_list[2]))
list3.append(new_op_list[3]*2)
list3.append(sum(new_op_list[:4]))
print(list3)
