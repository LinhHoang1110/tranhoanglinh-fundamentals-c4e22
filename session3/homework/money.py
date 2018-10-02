sizes = [5,7,300,90,24,50,75]
print("Hello, my name is Linh and here is my flock: ")
print(sizes)
print("Now my biggest sheep has size",max(sizes),"let's shear it")

a = sizes.index(max(sizes))
sizes[a] = 8

print("After shearing, here is my flock: ")
print(sizes)
print("\n")

for j in range(1,3):
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

print("MONTH 3: ")    
for a in range(len(sizes)):
    sizes[a]+=50
print("One month has passed, now here is my flock: ")
print(sizes)
print("\n")

s = 0

for b in range(len(sizes)):
    s += sizes[b]
print("My flock has size in total: ",s)    
print("i would get",s,"* 2$ = ", s*2,"$")

