data = 'myprogram.txt'

# Extracting the substring 'gram'
print(data[5:9])

# Truncate '.txt' from the data
print(data.rstrip('.txt'))

# Extract the middle character of the string
data = 'myprogram.txt'
middle = int(len(data)/2)
print(data[middle])