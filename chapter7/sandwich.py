# 7-8 熟食店：创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；
# 再创建一个名为finished_sandwiches的空列表。遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，
# 如I made your tuna sandwich，并将其移到列表finished_sandwiches。所有三明治都制作好后，打印一条消息，将这些三明治列出来。


# 7-9 五香烟熏牛肉(pastrami)卖完了：使用为完成练习7-8而创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。
# 在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个while循环将列表sandwich_orders中的'pastrami'都删除。
# 确认最终的列表finished_sandwiches中不包含'pastrami'。

print("pastrami sandwich is sell out")
sandwich_orders=["A sandwich","pastrami sandwich","B sandwith","pastrami sandwich","C sandwith","pastrami sandwich"]
finished_sandwiches=[]

while "pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("pastrami sandwich")
while sandwich_orders:
    for sandwich in sandwich_orders:
        print("I made your"+sandwich)
        sandwich_orders.remove(sandwich)
        finished_sandwiches.append(sandwich)
print(finished_sandwiches)