if 1+1 == 2:
    print("1+1=2")
elif 1+1 == 3:
    print("1+1=3")
else:
    print("1+1!=2")

num = int(input("请输入一个整数："))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")


age = int(input("请输入年龄："))
print(f"你的年龄是{age}岁")
if age >= 18:
    print("成年")
else:
    print("未成年")
