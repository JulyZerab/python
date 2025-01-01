#（1）初始化变量
i=0
while i<3: # (2) 条件判断
    # (语句块)
    user_name=input('请输入用户名：')
    user_password=input('请输入密码：')
    # 登录操作，if....else....
    if user_name=='ysj' and user_password=='888888':
        print('登录成功。')
        # 需要改变循环变量，目的为了退出循环
        i=8 # 在第三行判断i=8时，False，会退出整个while循环，改变变量
    else:
        if i<3:
            print('用户名或密码错误，您还有',2-i,'次机会！')
        i+=1 # 改变变量

# 单分支判断
if i==3:
    print('三次均输入错误！')


