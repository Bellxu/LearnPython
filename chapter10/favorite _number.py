# 10-11 喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number!It's _____.”。

import json
try:
    number=int(input("请输入你最喜欢的数字"))
except ValueError:
    print("请输入数字类型")
else:
    file_name="faccorite_number.json"
    with open(file_name,"w") as file_obj:
        json.dump(str(number),file_obj)