# 直接使用[]创建列表
lst=['hello','world','98','100.5']
print(lst)

# 使用内置函数list()创建列表
lst2=list('helloworld')
lst3=list(range(1,10,2))
print(lst2)
print(lst3)

# 对列表的操作符、运算符、函数
print(lst+lst2+lst3) # 序列中的相加操作
print(lst*3) # 列表的相乘操作
print(len(lst))
print(max(lst))
print(min(lst))
print(lst2.count('o'))
print(lst2.index('o'))

# 列表的删除操作
lst4=[10,20,30,40]
print(lst4)
del lst4
# print(lst4) # NameError: name 'lst4' is not defined


