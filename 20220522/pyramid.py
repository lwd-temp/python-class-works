longest = int(input("请输入打印图形高度："))
for i in range(1, longest + 1):
    print(("*"*(2*i-1)).center(2*longest-1))
