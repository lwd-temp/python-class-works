# 第五题
p = eval(input("请输入A商品当天的固定销售数量："))
n = 0
while p > 0:
    a = int(input("请输入当前顾客的购买数量："))
    if p >= a:
        p -= a
    else:
        p = 0
    n += 1
print("当天有{}位顾客买到了A商品".format(n))
