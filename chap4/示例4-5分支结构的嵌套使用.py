answer=input('请问，您喝酒了吗？')
if answer=='y':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('构不成酒驾，祝您一路平安')
    elif proof<80:
        print('您已构成酒驾，请不要开车！')
    else:
        print('已构成醉驾！')
else:
    print('你走吧，没你啥事。')