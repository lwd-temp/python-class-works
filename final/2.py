print("学号：201200131013 姓名：唐宇钧")
words = []
for i in range(1, 6):
    words.append(input("请输入第%d个单词：" % i))
print("输入的5个单词是："+str(words))
print("首字母是元音的单词有：")
for word in words:
    if word[0].lower() in "aeiou":
        print(word)
