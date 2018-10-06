quizex4= {
    "title": ["Estimate this anwer (exact calculation not needed)","jack scored these mark in 5 math test: 49, 81, 72, 66 and 52."],
    "question": ["if x =8, then what is the value of 4(x+3)? ","What is the mean? "],
    "choices": ["1. 35","2. 36","3. 40","4. 44","1. about 55","2. about 65","3. about 75","4. about 85"],
    "right choice": [3,2],
    "right answer": 0 
}

print(quizex4["question"][0])


for i in range(quizex4["choices"].index("1. about 55")):
    print(quizex4["choices"][i])
a = int(input("your choice: "))
if a == quizex4["right choice"][0]:
    print("Bingo")
    quizex4["right answer"]+= 1
else:
    print(":(")

print(quizex4["title"][0])
print(quizex4["title"][1])
print(quizex4["question"][1])

for j in range(quizex4["choices"].index("1. about 55"),len(quizex4["choices"])):
    print(quizex4["choices"][j])

b = input("your choice: ")
if b == quizex4["right choice"][1]:
    print("Bingo")
    quizex4["right answer"]+= 1
else:
    print(":(")    

print("you correctly answer",quizex4["right answer"],"out of 2 question")