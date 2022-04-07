n = int(input('Enter the Number: '))
f = [0, 1]
if n == 1:
    print(f)
else:
    for i in range(n-1):
        s = f[-2] + f[-1]
        f.append(s)
    print(f)
