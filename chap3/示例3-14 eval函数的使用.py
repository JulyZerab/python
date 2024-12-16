s='3.14+3'
print(s,type(s))
x=eval(s) # 使用eval函数去掉字符串左右的引号
print(x,type(x))

# eval函数经常和input函数一起使用，用来获取用户输入的数值

age=eval(input('请输出您的年龄：'))
print(age,type(age))

height=eval(input('请输入您的身高：'))
print(height,type(height))

hello='北京欢迎你'
print(hello)
print(eval('hello'))