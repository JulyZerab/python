luck_number=8 # 创建一个整形变量，并为其赋值为8

my_name = "JulyZebra" #字符串类型的变量

print("lick_number的数据类型是：",type(luck_number))
print(my_name,'的幸运数字是',luck_number)


# python动态修改变量的数据类型，通过赋不同类型的值就可以直接修改
no=number=1024
print(no,number)
print(id(no))   # id()查看对象的内存地址1979425236144
print(id(number)) # 1979425236144