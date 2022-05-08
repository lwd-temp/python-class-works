# 数学运算符
print(1 + 1)
print(1*2)
print(1/2)
print(1-2)
print(1 % 2)
print(1**2)
print(1//2)
# 字符串运算
print('Hello' + 'World')
print('Hello' * 3)
# 元组
print((1, 2, 3)+(4, 5, 6))

a = '3'
b = 3
print(a*b)

for i in range(1, 8, 2):
    print('@'*i)

# 7 1*1 2*3 3*5 4*7
for i in range(1, 5):
    print((str(i)*(2*i-1)).center(7, ' '))

# 比较运算
print(1 > 2)
print(1 < 2)
print(1 == 2)
print(1 != 2)
print(1 >= 2)
print(1 <= 2)
# 逻辑运算
print(1 and 2)
print(1 or 2)
print(not 1)
# 成员运算
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
# 身份运算
print(1 is 1)
print(1 is not 1)
# 赋值运算
a = 1
a += 1
print(a)
a -= 1
print(a)
a *= 1
print(a)
a /= 1
print(a)
a //= 1
print(a)
a %= 1
print(a)
a **= 1
print(a)

# 控制结构
# if语句
a = 1
if a == 1:
    print('a等于1')
elif a == 2:
    print('a等于2')
else:
    print('a不等于1或2')
# for语句
for i in range(1, 10):
    print(i)
# while语句
i = 1
while i < 10:
    print(i)
    i += 1
# break语句
for i in range(1, 10):
    if i == 5:
        break
    print(i)
# continue语句
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
# pass语句
for i in range(1, 10):
    pass
# 缺省语句
a = 1
if a == 1:
    pass
else:
    print('a不等于1')
# try语句
try:
    print(1/0)
except ZeroDivisionError:
    print('除数不能为0')
# finally语句
try:
    print(1/0)
except ZeroDivisionError:
    print('除数不能为0')
finally:
    print('无论是否发生异常都会执行')
# with语句
# with open('test.txt', 'r') as f:
#     print(f.read())
# 语句块


def test():
    print('test')


test()
# 函数


def test(a, b):
    print(a+b)


test(1, 2)
# 可变参数


def test(*args):
    print(args)


test(1, 2, 3, 4, 5)
# 关键字参数


def test(name, age):
    print(name, age)


test(age=18, name='张三')
# 可变参数和关键字参数


def test(*args, **kwargs):
    print(args, kwargs)


test(1, 2, 3, name='张三', age=18)
# 函数返回值


def test():
    return 1, 2, 3


a, b, c = test()
print(a, b, c)
# 函数的参数传递


def test(a, b):
    a = a+b
    print(a)


a = 1
b = 2
test(a, b)
print(a, b)

# 类型转换
# int()
# float()
# str()
# bool()
# list()
# tuple()
# dict()
# set()
# frozenset()
# chr()
# ord()
# bin()
# oct()
# hex()
