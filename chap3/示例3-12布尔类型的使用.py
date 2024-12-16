x=True
print(x)
print(type(x))
print(x+10) # 11
print(False+10) # 10
print('------------------')
print(bool(10)) # 测试整数10的布尔值为True
print(bool(0),bool(0.0)) # 0的布尔值为False
# 非0整数的布尔值为True
print(bool('北京欢迎你')) # True
print(bool('')) # False
# 所有非空字符串的布尔值都是True
print(bool(False)) # False
print(bool(None)) # False
