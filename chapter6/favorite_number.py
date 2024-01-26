# 6-2 喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键；
# 想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。打印每个人的名字和喜欢的数字。
# 为让这个程序更有趣，通过询问朋友确保数据是真实的。
favorite_number={
    "Bell":1,
    "Bob":2,
    "Candy":3,
    "Dincy":4,
    "Ellel":5
    }
print("Bell"+" favoriteNumber is "+str(favorite_number["Bell"]))
print("Bob"+" favoriteNumber is "+str(favorite_number["Bob"]))
print("Candy"+" favoriteNumber is "+str(favorite_number["Candy"]))
print("Dincy"+" favoriteNumber is "+str(favorite_number["Dincy"]))
print("Ellel"+" favoriteNumber is "+str(favorite_number["Ellel"]))
del favorite_number["Bell"]
favorite_number["Ferend"]=6
print(favorite_number)