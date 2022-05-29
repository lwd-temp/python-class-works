# 第六题
n = int(input("输入n："))
s = 0
for i in range(1, n+1):
    x = 0
    for j in range(1, i+1):
        x = x+j
    s = s+x
print(s)
