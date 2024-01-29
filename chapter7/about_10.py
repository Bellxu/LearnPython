# 7-3 10的整数倍：让用户输入一个数字，并指出这个数字是否是10的整数倍。

number=input("请输入一个数字: ")
if int(number) % 10 ==0:
    print(number+"是10的整数倍")
else:
    print(number+"不是10的整数倍")