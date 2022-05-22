score = int(input("请输入成绩："))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("E")

try:
    zerodivision = 1/0
except ZeroDivisionError:
    print("ZeroDivisionError")

s = 0
n = 1
while n <= 100:
    s = s + n
    n = n + 1
print(s)

t = 0
n = 1
while n < 10:
    t = t+n
    n = n+1
print(n, t)
