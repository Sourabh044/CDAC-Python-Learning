# even numbers List
list_ex = list([x for x in range(11) if x%2==0])
# Custom Tuple 
tuple_ex = (2,3,'Hello',5,['Sourabh',8351,234],8)
# Odd number set
set_ex = set([x for x in range(11) if x%2!=0])
# 
print('Traversing The list: ', end=" ")
for i in list_ex:
    print(i,end=" ")
print('\n')
# 
print('Traversing The tuple: ', end=" ")
for i in tuple_ex:
    print(i,end=" ")
print('\n')
# 
print('Traversing The set: ', end=" ")
for i in set_ex:
    print(i, end=" ")    
print('\n')