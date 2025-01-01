for i in range(1,4): # 外层循环控制行数
    for j in range(1,5): # 内层循环控制列数
        print('*',end='')
    print() # 空的print语句，作用是换行
print('--------------------')

for i in range(1,6):
    for j in range(1,i+1): # *的个数与行数相同，range(1,2)第二行，range(1,3)第三行
        print('*',end='')
    print() # 空的print语句，进行换行

