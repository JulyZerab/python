number=eval(input('请输入您的中奖号码：'))
# if..else
if number==987654:
    print('恭喜您，中奖了！')
else:
    print('很遗憾，您未中奖！')

print('------以上代码可以使用条件表达式进行简化------')
result='恭喜您中奖了！' if number==987654 else '您未中奖！'
print(result)

print('恭喜您中奖了！' if number==987654 else '您未中奖！')








