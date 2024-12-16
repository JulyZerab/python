x=20
y=10
x=x+y # 将x+y的和赋值给x，x的值为30
print(x)
x+=y # 40 相当于x=x+y
print(x)
print('x减y-------------')
x-=y
print(x)
print('x乘y-------------')
x*=y
print(x,type(x))
print('x除以y-------------')
x/=y
print(x,type(x))
print('x整除y-------------')
x//=y
print(x,type(x))
print('x取模y-------------')
x%=y
print(x,type(x))
print('x幂等y-------------')
x**=y
print(x,type(x))

# python支持链式赋值
a=b=c=100
print(a,b,c)

# python支持系列解包赋值
a,b=10,20 # 相仿于执行了两次操作a=10,b=20
print(a,b)

print('--------如何交换两个变量的值呢？--------')
a,b=b,a # 将a的值赋值给b，将b的值赋值给a
print(a,b)

