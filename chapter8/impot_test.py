# 8-16 导入：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一个文件中。在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# importmodule_name
# frommodule_name importfunction_name
# frommodule_name importfunction_name as fn
# importmodule_name asmn
# frommodule_name import *

# import message
# from message import display_message
# message.display_message()
# from message import display_message as ma
# ma()
# import message as ma
# ma.display_message()
from message import *
display_message()

