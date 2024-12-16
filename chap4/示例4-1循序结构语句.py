# 赋值运算符的顺序，从右到左
name='张三'
age=20
a=b=c=30

print(name)
print(age)
print(a,b,c)
print('-'*10,'输入/输出语句也是典型的顺序结构','-'*10)
name=input('请输入您的姓名：')
age=eval(input('请输入您的年龄：'))
luck_number=eval(input('请输入您的幸运数字：'))
print(name)
print(age)
print(luck_number)
