#factorial of n
n = int(input("Enter a number: "))
facl = 1
for i in range(1,n+1):
    facl *= i # facl = facl * i
print(facl)
