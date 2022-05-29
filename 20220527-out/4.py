# 第四题
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ls = []
for x in a:
    s = 1
    for y in x:
        s *= y
    ls.append(s)
print(ls)
