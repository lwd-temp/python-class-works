endat = int(input("请输入要计算的数值n："))
sum = 0
n = 1
while n <= endat:
    sum = sum + n
    n = n + 1
print("1+...+n的值为：", sum)

endat = int(input("请输入要计算的数值n："))
sum = 0
for i in range(1, endat+1):
    sum = sum + i
print("1+...+n的值为：", sum)
