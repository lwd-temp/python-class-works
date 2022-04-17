list = ['a', 'b', 'c', 'd', 'e']  # 列表
print(list)
list[1] = 'B'  # 修改列表元素
print(list)
list[0:3] = ['A', 'B', 'C']  # 修改列表元素
print(list)
del list[0]  # 删除列表元素
print(list)
list.append('f')  # 在列表末尾添加元素
print(list)
list.insert(0, 'a')  # 在列表指定位置添加元素
print(list)

tup0 = ()  # 空元组
print(tup0)
tup1 = ('a', 'b', 'c', 'd')  # 元组
print(tup1)
tup2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 元组
print(tup2)
tup3 = (1,)  # 元组
print(tup3)
tup4 = (1)  # int
print(tup4)

tup5 = (1, 'a', [1, 2, 3])  # Read-only

try:
    tup5[0] = 'a'
except Exception as e:
    # 'tuple' object does not support item assignment
    print(e)

listtup = [1, 2, 3]
tup6 = (1, listtup)
print(tup6)
listtup.append(4)
print(tup6)

tup7 = (1, 2, 3)
try:
    del tup7[0]
except Exception as e:
    print(e)

del tup7

try:
    print(tup7)
except Exception as e:
    print(e)

dict1 = {'a': 1, 'b': 2, 'c': 3}  # 字典 无序
print(dict1['a'])
dict1['a'] = 'A'
print(dict1)
dict1.update({'d': 4})  # 添加
print(dict1)

for key in dict1:
    print(key)
    print(dict1[key])

dict1.clear()

print(dict1)

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # 集合，无序，不重复
set2 = set()  # 空集合
set3 = set(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # 集合
