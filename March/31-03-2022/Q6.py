y = ((10,10,10,12),(30,45,56,45),(81,80,92,56),(1,2,3,4))
maximum_list = []
minimum_list = []
average_list = []
for tup in y:
    maximum_list.append(max(tup))
    minimum_list.append(min(tup))
    average_list.append(sum(tup)/len(tup))
print(minimum_list)
print(maximum_list)
print(average_list)