# 倒三角形
# 1-->5 range(1,6),2-->4 range(1,5),3-->3 range(1,4)
for i in range(1,6):
    for j in range(1,7-i):
        print('*',end='')
    print()

print('--------------------------')

# 等腰三角形
'''
****$
***$$$
**$$$$$
*$$$$$$$
$$$$$$$$$
'''
for i in range(1,6):
     for j in range(1,6-i):
         print(' ',end='')
     # 1,3,5,7....等腰三角形range(1,2),range(1,4),range(1,6),range(1,8)
     for k in range(1,i*2):
         print('$',end='')
     print()

