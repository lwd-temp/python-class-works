# 第一题
s = 0
for x in range(200, 501):
    if x % 3 == 0 and x % 5 != 0:
        s += x
print(s)
