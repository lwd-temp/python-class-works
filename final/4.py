import random

print("学号：20120013302 姓名：赵晓辉")

# 列表承载生成题目
quizsList = []

while len(quizsList) <= 50:  # 判断题目数量是否超过50道
    quiz = str(random.randint(0, 19)) + "+" + \
        str(random.randint(0, 19)) + "="  # 生成题目
    if quiz in quizsList:  # 判断题目是否重复
        pass  # 如果重复，则跳过
    else:
        quizsList.append(quiz)  # 如果不重复，则添加到列表中

for i in range(0, 5):  # 循环5次
    lineString = ""  # 初始化空字符串
    for fivequiz in quizsList[i*5:(i+1)*5]:  # 每5道题
        lineString += fivequiz + "\t"  # 拼接，使用制表符
    print(lineString)
