x=10
y=3
z=x/y # 执行除法运算，并将结果赋值给z
print(z,type(z)) # 隐式转换

# float类型转成int类型，只保留整数类型
print('float类型转成int类型：',int(3.14))
print('float类型转成int类型：',int(3.9))
print('float类型转成int类型：',int(-3.14))
print('float类型转成int类型：',int(-3.9))

# 将int类型转成float类型
print('将int类型转成float',float(3))

# 将str转成int类型
print(int('100')+int('200'))
# 将字符串转成int或float时报错的情况
#print(int('18a'))
#print(int('3.14'))

#print(float('45.987a'))


# chr()ord()一对
print(ord('秦')) # 在unicode表中对应的数值
print(chr(31206))


# 进制之间的转换
print('十进制转成十六进制：',hex(31206))
print('十进制转成八进制：',oct(31206))
print('十进制转成二进制：',bin(31206))

