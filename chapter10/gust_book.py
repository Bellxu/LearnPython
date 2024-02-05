# 10-4 访客名单：编写一个while循环，提示用户输入其名字。
# 用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
import sys
sys.text_encoding="utf-8"
more=True
while more:
    name=input("请输入用户\n")
    with open("guest_book.txt","a") as file_object:
        file_object.write(name+"\n")
        print(name+"记录成功")
        more_message=input("还有要记录的人名吗(yes/no)")
        if more_message=="no":
            more=False