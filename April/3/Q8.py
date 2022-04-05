import os
os.system('cls')
reversed_words = []
Words = ['mam','apple','name','cac','dad','mom']
reversed_words = list(filter(lambda x :list(reversed(x))==list(x),Words))

print(reversed_words)