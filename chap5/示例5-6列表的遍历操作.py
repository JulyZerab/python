lst=['hello','world','python','php']
# 使用遍历for循环遍历列表元素
for item in lst:
    print(item)

# 使用for循环，range()函数，len()函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'--->',lst[i])

# 使用enumerate()函数
for index,item in enumerate(lst): # index自己起的名字，item自己定义的变量名
    print(index,item) # index是序号，不是索引

for index,item in enumerate(lst,start=1): # 手动设置序号的起始值
    print(index,item)

for index,item in enumerate(lst,1): # 手动设置序号的起始值
    print(index,item)



