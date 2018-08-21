no = int(input("Enter a number: "))


# total = sum(range(0,no+1))
# print("result: ", total)



total = 0
for i in range(no + 1):
    total = total + i # total += i


print("result: ", total)