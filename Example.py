
# Write a Python program to find the missing number in a given array of numbers between 10 and 20.
# [10 11 12 13 14 16 17 18 19 20]

# listnum = [10 ,11, 12, 13, 14, 16, 17, 18, 19, 20]

# # listttotw = [x for x in range(10,21)]
# nummissing = list()
# for i in range(10,21):
#     if not i in listnum:
#         nummissing.append(i)

# print('Numbers that are missing from the array are: \n',nummissing)

# for i in nummissing:
#     for x in listnum:
#         if x-1==i:
#             # print(listnum.index(x))
#             listnum.insert(listnum.index(x),i)

# print(listnum)

# Write a Python program to remove all duplicate elements from a given array and returns a new array?
# [1 3 5 1 3 7 9]

arraynum = [1 ,3, 5, 1, 3, 7, 9]

for i in range(len(arraynum)):
    
    try:
        for x in range(i+1,len(arraynum)):
            if arraynum[i] == arraynum[x]:
                arraynum.pop(x)
    except IndexError as e:
         pass

print(arraynum)
         




















