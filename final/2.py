print("学号：201200131013 姓名：唐宇钧")

# 列表承载输入内容
wordsList = []

for i in range(1, 6):
    wordsList.append(input("请输入第%d个单词：" % i))  # 输入单词

print("输入的5个单词是："+str(wordsList))  # 打印输入的单词

print("首字母是元音的单词有：")
for word in wordsList:
    if word[0].lower() in "aeiou":  # 判断首字母是否为元音，lower()将大写转换为小写
        print(word)
