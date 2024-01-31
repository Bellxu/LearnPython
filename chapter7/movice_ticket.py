# 7-5 电影票：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3～12岁的观众为10美元；
# 超过12岁的观众为15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。


while True:
    age=int(input("你今年多大了?"))
    price=""
    if age <3:
        price="免费"
    elif age <12:
        price="10美元"
    else:
        price="15美元"
    print("看电影的票价为"+price)
    break
