S1 = int(input('Enter the Number of elements in the First set: '))
s1_set = set()
for i in range(S1):
    se = int(input("Enter the Element: "))
    s1_set.add(se)
sum_s1 = sum(s1_set)
minimum_s1 = min(s1_set)
maximum_s1 = max(s1_set)
# S1 = set(s1_set)
# print(type(S1))
print(s1_set)

S2 = int(input('Enter the Number of elements in the Second set: '))
s2_set = set()
for i in range(S2):
    se = int(input("Enter the Element: "))
    s2_set.add(se)
sum_s2 = sum(s1_set)
minimum_s2 = min(s2_set)
maximum_s2 = max(s2_set)
# S2 = set(s2_set)
# print(type(S1))
print(s2_set)
# len
print("The len of the First set is",len(s1_set))
print("The len of the Second set is",len(s2_set))
# min
print("The Minimum element in First set is",minimum_s1)
print("The Maximum element in First set is",maximum_s2)
# set 2
print("The minimum element in Second set is",minimum_s2)
print("The minimum element in Second set is",maximum_s2)
# sum
print("The sum of all elements in the First set is",sum_s1)
print("The sum of all elements in the Second set is",sum_s2)
print("The sum of both the set is",sum_s1+sum_s2)
# union
un = s1_set|s2_set
print('The Union is')
print(un)
# difference
diff = s1_set.difference(s2_set)
print('The difference is ',diff,sep="\n")
# intersection
inter = s1_set.intersection(s2_set)
print('The intersection is ',inter,sep="\n")
print()
# Symmetric Difference
SD = s1_set.symmetric_difference(s2_set)
# issuperset
if s1_set.issuperset(s2_set):
    print('s1_set is Superset of s2_set')
elif s2_set.issuperset(s1_set):
    print("No, Second Set is the SuperSet of First Set")
else:
    print('No SuperSet')
#  issubset
if s1_set.issubset(s2_set):
    print('s1_set is Subset of s2_set')
elif s2_set.issubset(s1_set):
    print("No, Second Set is the Subset of First Set")
else:    
    print('No SubSet')