sizes = [5,7,300,90,24,50,75]
print("Hello my name is Linh and these are my ship sizes: ")
print(sizes)


print("Now my biggest sheep has size ",max(sizes),"let's shear it")



a = sizes.index(max(sizes))

sizes[a] = 8

print("After shearing, here is my flock :")
print(sizes)

