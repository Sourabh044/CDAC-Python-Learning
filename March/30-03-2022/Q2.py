a = ['Mobile','Laptop',100,'Camera',310.28,'Speakers',27.00,'Television',1000,'Laptop Case','Camera Lens']
# Sorting String elmenets in a new list
stringElements = [string for string in a if type(string)==str]
print("string Elements of the list")
print(stringElements)
# Sorting Int elements in a new list
intElements = [intItems for intItems in a if type(intItems)==int or type(intItems)==float]
print("int and float Elements of the list")
print(intElements)
# Applying Sorting Functions
# Sorting String
print("After Sorting Ascending")
stringElements.sort()
print(stringElements)
stringElements.sort(reverse=True)
print("After Sorting Descending")
print(stringElements)
# Sorting int
print("Lowest To Highest")
intElements.sort()
print(intElements)
intElements.sort(reverse=True)
print("Highest to Lowest")
print(intElements)


