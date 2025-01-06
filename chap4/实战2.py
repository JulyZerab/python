# (1)初始化变量
answer='y'
# (2)条件判断
while answer=='y':
    # (3)循环操作，语句块
    print('----------------欢迎使用10086查询功能')
    print('1.查询当前余额')
    print('2.查询当前的剩余流量')
    print('3.查询当前的剩余通话时长')
    print('0.退出系统')
    choice=input('请输入您要执行的操作：') # input的结果是字符串类型
    if choice=='1':
        print('当前余额为88374元。')
    elif choice=='2':
        print('当前剩余流量为2338G')
    elif choice=='3':
        print('当前剩余通话时长为2323分钟')
    elif choice=='0':
        print('程序退出，谢谢您的使用！')
        break
    else:
        print('您输入的有误，请重新输入')
    # (4)改变变量
    answer=input('还继续操作吗？y/n')
else:
    print('程序退出')







