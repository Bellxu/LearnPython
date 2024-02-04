
# 9-12 多个模块：将User类存储在一个模块中，并将Privileges和Admin类存储在另一个模块中。
# 再创建一个文件，在其中创建一个Admin实例，并对其调用方法show_privileges()，以确认一切都依然能够正确地运行。
from user import User

class Privileges():
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges=Privileges()