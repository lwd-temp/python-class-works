print("学号：20120013302 姓名：赵晓辉")

nums = ""
for i in range(100, 1000):
    before = int(i)
    after = int(str(i)[1:3]+str(i)[0])
    if after-before == 432:
        nums = nums+str(i)+" "

print("原三位数为:"+nums)
