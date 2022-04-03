# 我是一行注释

'''
我是
多行
注释
'''

n1 = input("请输入：")  # 获取用户输入并赋值给变量n1

print("您好！", n1)  # 打印您好！和变量n1的值

print("您好！", end="")  # 打印您好！，不换行
print(n1)  # 打印变量n1的值

print("您好！"+" "+str(n1))  # 打印您好！和变量n1的值（在此之前转化为str类型）

i_am_a_super_long_variable_name = "Hello World!"  # 定义变量
I_AM_number_1 = 1

# 让我们稍微混乱一下，工作中别这么干
变量一 = "你好，世界！"
print(变量一)

打印 = print
打印("您好！", n1)
打印(变量一)

print(i_am_not_exist)  # 打印不存在的变量
# NameError: name 'i_am_not_exist' is not defined
