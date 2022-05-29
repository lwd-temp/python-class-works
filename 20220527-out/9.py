# 第七题
s = input("输入一段英文文字：")
n = 0
for a in s:
    if a in ".!?":
        n += 1
print(n)
