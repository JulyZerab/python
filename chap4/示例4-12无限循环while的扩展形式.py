# 1-100之间的累加和
s=0 # 存储累加和
i=1 # (1)初始化变量
while i<=100: # (2)条件判断
    s+=i # (3)语句块
    # (4)改变变量
    i+=1 # 相当于i=i+1
else:
    print('1-100的累加和为：',s)
