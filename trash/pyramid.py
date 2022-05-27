# 金字塔打印

while True:
    choice = int(input("请输入打印图形的行数："))
    if choice < 0:
        print("请输入正数！")
    if choice == 0:
        break
    if choice > 0:
        maxlen = 2*choice-1
        for i in range(1, choice+1):
            print((str(i)*(2*i-1)).center(maxlen, " "))
