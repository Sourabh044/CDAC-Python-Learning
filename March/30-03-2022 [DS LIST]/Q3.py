# Taking 10 numbers from the user
numbers = []
for i in range(10):
    a = int(input('Enter Number :'))
    numbers.append(a)
numberSum = sum(numbers)
minNumber = min(numbers)
maxNumber = max(numbers)
print('Sum of the Numbers =',numberSum)
print('Minimum Number is',minNumber)
print('Maximum Number is',maxNumber)