# 计算100以内能被3或7整除的数字
数字们 = []
for 一个 in range(1, 101):
    if 一个 % 3 == 0 or 一个 % 7 == 0:
        数字们.append(一个)

# 格式化输出
输出字符串 = ""
for 另一个 in 数字们:
    输出字符串 = 输出字符串 + str(另一个) + ","
输出字符串 = 输出字符串[:-1]
print(输出字符串)
# outputstr = ','.join(str(n) for n in 数字们)
# print(outputstr)

# 求和
print("数字和为", sum(数字们))
