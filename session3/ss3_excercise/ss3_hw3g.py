
sizes = [5, 7, 300, 90, 24, 50, 75]
sizes_len = len(sizes)
print("Hello, my name is Cuong and these are my ship sizes:", sizes)


# max_size = max(sizes)
# print('Now my biggest sheep has size ', max_size, 'Let shear it.')
# print("* " * 20)

# sizes[sizes.index(max_size)] = 8
# print('After shearing, here is my flock: ', sizes)
# print("* " * 20)

for j in range(1,3):
    print('MONTH ',j,':',sep='')
    for i in range(sizes_len):
        sizes[i] += 50
    print('One month has passed, now here is my flock ', sizes)
    max_size = max(sizes)
    print('Now my biggest sheep has size ', max_size, 'Let shear it.')
    sizes[sizes.index(max_size)] = 8
    print('After shearing, here is my flock: ', sizes)

print('MONTH :3')
for i in range(sizes_len):
    sizes[i] += 50
print('One month has passed, now here is my flock ', sizes)
total = 0
for i in range(sizes_len):
    total += sizes[i]
price = total * 2
print('My flock has size in total: ',total)
print('I would get: ',total,'* 2$ = ',price,'$',sep='')