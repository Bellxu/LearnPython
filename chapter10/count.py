# 10-6 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数字。
# 在这种情况下，当你尝试将输入转换为整数时，将引发ValueError异常。
# 编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。
# 在用户输入的任何一个值不是数字时都捕获ValueError异常，并打印一条友好的错误消息。对你编写的程序进行测试：先输入两个数字，再输入一些文本而不是数字。]
# print("接下来需要输入两个数字,我们会把两个数字相加")
# try:
#     number1=int(input("请输入第一个数字\n"))
# except ValueError:
#     print("请输入数字")
# try:
#     number2=int(input("请输入第二个数字\n"))
# except ValueError:
#     print("请输入数字")
# print(number1+number2)

# 10-7 加法计算器：将你为完成练习10-6而编写的代码放在一个while循环中，让用户犯错（输入的是文本而不是数字）后能够继续输入数字。

print("接下来需要输入两个数字,我们会把两个数字相加")
number1=0
number2=0
put_number1=True
put_number2=True
while put_number1:
    try:
        number1=int(input("请输入第1个数字\n"))
    except ValueError:
        print("请输入数字")
    else:
        put_number1=False

while put_number2:
    try:
        number2=int(input("请输入第2个数字\n"))
    except ValueError:
        print("请输入数字")
    else:
        put_number2=False
print(number1+number2)