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


# 6-10 喜欢的数字：修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来
favorite_numbers={
    "Bell":[1,100],
    "Bob":[2,200,2000],
    "Candy":[3],
    "Dincy":[4,14,44],
    "Ellel":[1,5,10,15]
    }

for name,numbers in favorite_numbers.items():
    
    lenz=len(numbers)
    if lenz<1:
        print(name +"favorte number is None")
    else:
        if lenz ==1:
            print(name +"favorte number is")
        else:
            print(name +"favorte numbers are")
        for number in numbers:
            print(number)