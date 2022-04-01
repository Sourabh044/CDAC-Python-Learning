# Taking number from the user
f = int(input("Enter Number to Find Factorial: "))
factorial = 1
i = f
# Calculating Factorial
while(i!=0):
    factorial *= i
    i -= 1
# printing the factoring of the number
print("The Factorial of Number is:",factorial)