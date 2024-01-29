# 6-9 喜欢的地方：创建一个名为favorite_places的字典。
# 在这个字典中，将三个人的名字用作键；
# 对于其中的每个人，都存储他喜欢的1～3个地方。
# 为让这个练习更有趣些，可让一些朋友指出他们喜欢的几个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

favorite_places={
    "Bell":["四川","上海"],
    "Candy":["云南","贵州","四川"],
    "Dell":["北京"]
    }

for name,places in favorite_places.items():
    if len(places)>1:
        print(name+" favorite places are ")
    else:
        print(name+" favorite places is")
    for place in places:
        print(place)