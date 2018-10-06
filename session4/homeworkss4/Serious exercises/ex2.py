prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for i in prices.keys():
    print(i)
    print("price: ",prices[i])
    print("stock: ",stock[i])
    print()

total = 0
for a in prices.keys():
    total = total + prices[a] * stock[a]
    
print("the money you would make if you sold all of your food is: ",total)    