import math
Degree_list = [0,30,45,90]
list_sin = [math.sin(math.radians(i)) for i in Degree_list]
list_cos = [math.cos(math.radians(i)) for i in Degree_list]
list_tan = [math.tan(math.radians(i)) for i in Degree_list]
# Printing values
print(list_sin)
print(list_cos)
print(list_tan)