import random

print("学号：20120013302 姓名：赵晓辉")

quizs = []

while len(quizs) <= 50:
    quiz = str(random.randint(0, 19)) + "+" + str(random.randint(0, 19)) + "="
    if quiz in quizs:
        pass
    else:
        quizs.append(quiz)

for i in range(0, 5):
    line = ""
    for quizcoll in quizs[i*5:(i+1)*5]:
        line += quizcoll + "\t"
    print(line)
