# Taking Number from User
a = int(input("Enter a Number: "))
# Printing the sum of 1 to N numbers
sum = 0
for i  in range(1,a+1):
    sum += i
print("The sum of 1 to",a,'Numbers is',sum)
# Printing Average
print("Average is :",sum/a)