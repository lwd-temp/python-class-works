print("学号：20120013302 姓名：赵晓辉")

# 最终输出字符串
outputString = ""

for i in range(100, 1000):  # 遍历所有三位数
    origNum = int(i)  # 原数
    fixedNum = int(str(i)[1:3]+str(i)[0])  # 处理后数字
    if fixedNum-origNum == 432:  # 求差值
        outputString = outputString+str(i)+" "  # 将符合条件的数字添加到输出字符串

print("原三位数为:"+outputString)
