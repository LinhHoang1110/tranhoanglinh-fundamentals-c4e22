while True:
    print("Wellcome to our shop!",end=' ' )

    cmds = ["C","R","U","D"]

    a = input("What do you want (C,R,U,D)? ")

    shops = ["T-Shirt","Sweater"]

    if a == cmds[1]:
        print("Our items: ",*shops)

    elif a == cmds[0]:    
    
        
        b = input("Enter new item: ")
        shops.append(b)
        print("Our items : ",*shops)
        new_shops = shops


    elif a == cmds[2]:
            c = int(input("Update position? "))
            d = input("New item: ")
            new_shops[c] = d
            print("Our items: ",*new_shops)

    elif a == cmds[3]:
            e = int(input("Delete position? "))
            new_shops.remove(new_shops[e])    
            print("Our items :",*new_shops)
            break

        


