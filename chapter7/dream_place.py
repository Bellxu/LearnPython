# 7-10 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit one place in the world,where would you go?”的提示，并编写一个打印调查结果的代码块。
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name?") 
    response = input("If you could visit one place in the world,where would you go")
    # 将答卷存储在字典中
    responses[name] = response 
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond?(yes/ no) ") 
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--- Poll Results ---")
for name,response in responses.items():
    print(name+" would like to climb "+response+".")