# Reduce
from functools import reduce
numbers = [2,7,1,8,2,4,5]
a = reduce(lambda x,y:x if x>y else y,numbers)
print(a)