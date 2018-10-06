quizex3 = {
    "question": "if x =8, then what is the value of 4(x+3)? ",
    "choices": ["1. 35","2. 36","3. 40","4. 44"],
    "right choice": 3 
}
while True:
    print(quizex3["question"])
    for i in quizex3["choices"]:
        print(i)
    a = int(input("your choice: "))

    if a == quizex3["right choice"]:
        print("Bingo")
        break
    else:
        print(":(")    