# 第七题
time = int(input("输入通话时间："))
fix = input("是否为固定套餐用户(y/n):")
if fix == 'y':
    fee = 50
    if time > 300:
        fee += (time-300)*0.1
else:
    fee = time*0.2
print("本月话费：{:.0f}".format(fee))
