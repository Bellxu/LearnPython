pizzas=["达美乐","棒约翰","必胜客"]
for pizza in pizzas:
    print("I like"+pizza+"pizza")
print(pizzas[0]+"is my favorite")
# 4-11
my_friend_pizzas=pizzas[:]
pizzas.append("乐凯撒")
my_friend_pizzas.append("不知道")

print("我最喜欢的披萨是")
for pizza in pizzas:
    print(pizza)

print("我朋友最喜欢的披萨是")
for pizza in my_friend_pizzas:
    print(pizza)

