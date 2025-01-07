s1='helloworld'
print('e在helloworld中存在吗?',('e'in s1))
print('v在helloworld中存在吗?',('v'in s1))

# not in的使用
print('e在helloworld中不存在吗?',('e'not in s1))
print('v在helloworld中不存在吗?',('v'not in s1))

# 内置函数的使用
print('len()',len(s1))
print('max()',max(s1)) # 按ASCII码值计算
print('min()',min(s1)) # 按ASCII码值计算

# 序列对象的方法 使用序列的名称，打点调用 称为方法
print('s.index():',s1.index('o')) # o在s1中第一次出现的索引位置
# print('s.index():',s1.index('v')) # ValueError: substring not found v在字符串中不存在
print('s.count():',s1.count('o')) # 统计o在字符串s1中出现的次数2次




