sizes = [5,7,300,90,24,50,75]
print("Hello my name is Linh and here is my flock: ")
print(sizes)

for j in range(1,4):
    print("MONTH",j,":")
    for i in range(len(sizes)):
        sizes[i] = sizes[i] + 50 
    print("One month has passed, now here is my flock")
    print(sizes)

    print("Now my biggest sheep has size",max(sizes),"let's shear it")

    a = sizes.index(max(sizes))
    sizes[a] = 8

    print("After shearing, now here is my flock: ")
    print(sizes)
    print("\n")
    new_sizes = sizes


    
