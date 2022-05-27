# 计算100以内能被3或7整除的数字
nums = []
for i in range(1, 101):
    if i % 3 == 0 or i % 7 == 0:
        nums.append(i)

# 格式化输出
outstr = ""
for n in nums:
    outstr = outstr + str(n) + ","
outstr = outstr[:-1]
print(outstr)
# outputstr = ','.join(str(n) for n in nums)
# print(outputstr)

# 求和
print("数字和为", sum(nums))
