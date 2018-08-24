

sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Cuong and these are my ship sizes:", sizes)
print("* " * 20)

max_size = max(sizes)
print('Now my biggest sheep has size ', max_size, 'Let shear it.')
print("* " * 20)

sizes[sizes.index(max_size)] = 8
print('After shearing, here is my flock: ', sizes)
print("* " * 20)


