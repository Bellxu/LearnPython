# 7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
left=input("请问有多少人用餐?")
left_number=int(left)
if left_number >8:
    print("没有空桌子了")
else:
    print("还有空桌子")