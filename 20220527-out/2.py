# 第二题
x = int(input("x="))
y = int(input("y="))
if x == y:
    print("请输入两个不同的正整数")
else:
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller):
        if x % i == 0 and y % i == 0:
            hcf = i
    print("两数的最大公因数是：", hcf)
