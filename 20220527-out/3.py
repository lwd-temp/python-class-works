# 第三题
x = eval(input("请输入PM2.5值："))
if type(x) is str:
    print("输入错误")
else:
    if x < 35:
        print("优")
    elif x < 75:
        print("良")
    elif x < 115:
        print("轻度污染")
    else:
        print("中重度污染")
