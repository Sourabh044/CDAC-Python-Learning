# Taking A string
estring = input('Enter a string: ')
no_of_characters = {}
estring = estring.lower()
list_char = set(estring) # To take only unique element
for char in estring:
    no_of_characters[char] = estring.count(char)
list_char = sorted(list(estring), reverse=True)
print(no_of_characters)
print(list_char)