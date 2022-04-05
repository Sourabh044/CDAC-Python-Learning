alphabets = ['A','B','C','D','E','F','G','H','I','U','O','Z','Q']
vowels = ['a','e','i','o','u']
vowels_extracted = list(filter(lambda x :x.lower() in vowels,alphabets))
print(vowels_extracted)