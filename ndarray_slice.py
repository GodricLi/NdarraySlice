# _*_ coding=utf-8 _*


import numpy as np

"""数组的索引与切片"""
# 数组
a = np.array(range(5))
b = np.array(range(15)).reshape((3, 5))  # 创建一个3列5行的数组

# 列表
li = [i for i in range(5)]
li2 = [[i for i in range(5)], [i for i in range(5, 10)], [i for i in range(10, 15)]]

"""切片
    数组的切片不会自动复制，而是创建一个视图，在切片的数组上修改会影响原数组值，
    使用copy()方法可以创建元素组的深拷贝
"""
print('----------切片----------')
print(li2)
print(a[2:])
c = a[0:2]
d = li[0:2]
c[0] = 20
d[0] = 10
print(a)  # 数组a[0]被修改了
print(li)  #
e = a[0:2].copy()  # 此时修改e不会影响a
e[0] = 30
print(a)    # a[0]没有被修改为 30


"""索引"""
print()
print('----------索引----------')
# 一维数组
print(a[2])
# 多维数组的索引
print(b[2, 1])  # [行,列]
# 多维列表的索引
print(li2[2][1])
