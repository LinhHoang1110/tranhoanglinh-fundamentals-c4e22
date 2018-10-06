quiz = {
    'stimulus':['today, c4e22 study','class has alot of boy'],
    'stem':'who is handsome?',
    'choices': ['0. quan','1.an','2.both of them','3.no one'],
    'rightchoice': 2
}

print(quiz['stimulus'][0],end=",")
print(quiz['stimulus'][1])
print(quiz['stem'])       
for i in quiz['choices']:
    print(i) 

a = int(input("your answer is? "))

if a == quiz['rightchoice']:
    print("that's right!")
else:
    print("you are wrong!")    