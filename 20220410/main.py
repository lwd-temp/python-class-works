# 我自己觉得有点阴间的赋值方法
from distutils.util import byte_compile


a = b = 1
c, d = 1, 2

# 数据类型

# int
number = 1
# float
number = 1.0
number = 1.456
number = 1.2e10
# complex
number = 1j
# bool
number = True
# str
number = '1'
# list
number = [1, 2, 3]
# tuple
number = (1, 2, 3)
# dict
number = {'a': 1, 'b': 2}
# set
number = {1, 2, 3}
# frozenset
number = frozenset({1, 2, 3})
# bytes
number = b'1'
# bytearray
number = bytearray(b'1')
# memoryview
number = memoryview(b'1')

string = "hello"

a_bool = True

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 有序

a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # 不变

a_dictionary = {a: 1, b: 2, c: 3, d: 4}  # 对应

a_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}  # 无序

a_complex = 3+5j
b_complex = complex(3, 5)

print(type(a_set))

string = "qwertyuiop"

# 字符串切片
print(string[0:5])
print(string[0:5:2])
print(string[0:])
print(string[:3])
print(string[:])
# 字符串访问
print(string[0])
print(string[-1])
print(string[-2])
# 转义符
print("\n")  # 换行
print("\t")  # 制表符
print("\b")  # 退格
print("\r")  # 回车
print("\f")  # 换页
print("\v")  # 垂直制表符
print("\\")  # 反斜杠
print("\'")  # 单引号
print("\"")  # 双引号

print("Python was started by \"Guido\"")
print("c:\\window\\app")
print(r"c:\window\app")

# 字符串格式化
print("%s" % "hello")
print("%d" % 123)
print("%f" % 123.456)
print("%.2f" % 123.456)
print("{a} {b} {c}".format(a=1, b=2, c=3))
print(f"{a} {b} {c}")