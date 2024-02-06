# 10-11 喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number!It's _____.”。

import json
file_name="faccorite_number.json"
with open(file_name) as file_obj:
    number=json.load(file_obj)
    print("I know your favorite number!It's"+str(number)+".")