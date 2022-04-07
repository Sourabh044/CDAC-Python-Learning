# name = 'Sourabh Chaudhary0' # 17 total, 6 vowels
name = input("Enter your Name: ")
vowels = ['a','e','i','o','u']
v,s,d,c = 0,0,0,0
for char in name:
    if char.isalpha():
        if char in vowels:
            v +=1
        else:
            c += 1
    elif char.isnumeric():
            d +=1
    elif char == ' ':
        s+=1
        
# Printing
print('Vowels = %d '%v)
print('Consonants = %d'%c)
print('Digits = %d'%d)
print('Space = %d'%s)