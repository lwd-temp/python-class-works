#num = int(input("请输入一个数："))
# if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
#    print(num, "在0-5或10-15之间")
# else:
#    print(num, "不在0-5或10-15之间")


# 1.能被4整除,但不能被100整除的年份(例如2008是闰年,1900不是闰年)
# 2.能被400整除的年份(例如2000年)也是闰年。
year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "是闰年")
else:
    print(year, "不是闰年")

h = float(input("身高："))
w = float(input("体重："))
bmi = w / (h * h)
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("非常肥胖")


pm2p5 = float(input("请输入pm2.5："))
if pm2p5 < 35:
    print("优")
elif pm2p5 < 75:
    print("良")
elif pm2p5 < 115:
    print("轻度污染")
elif pm2p5 < 150:
    print("中度污染")
elif pm2p5 < 250:
    print("重度污染")
else:
    print("严重污染")
