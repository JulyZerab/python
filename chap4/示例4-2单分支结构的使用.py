number=eval(input('请输入您的6位中奖号码：'))
# 使用if语句
if number==987654: # 等值判断
    print('恭喜您，中奖了！')

if number!=987654:
    print('很遗憾，您未中奖！')

print('------以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔类型------')
n=98 # 赋值操作
if n%2: # 98%2的余数为0，0的布尔值为False
    print(n,'是奇数') # 由于98%2的余数是0，所以该行代码不执行

if not n%2: # 98%2的余数0，0的布尔值为False,取反为True
    print(n,'为偶数')

print('---------判断一个字符串是否是空字符串---------')
x=input('请输入一个字符串：')
if x: # 在python中一切皆对象，每个对象都有一个布尔值，非空字符串的布尔值为True，空字符串的布尔值为False
    print('x是一个非空字符串')

if not x: # 空字符串的布尔值为False，取反为True
    print('x是一个空字符串')

print('-------表达式也也可以是一个单纯的变量------')
flag=eval(input('请输入一个布尔类型的值：True或False'))
if flag:
    print('flag的值为True')
if not flag:
    print('flag的值为False')

print('------如果使用if语句时，语句块中只有一行代码，可以将语句块直接写在冒号后面------')
a=10
b=5
if a>b:max=a
print('a和b的最大值为：',max)
