# 9-3 用户：创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。
# 在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；
# 再定义一个名为greet_user()的方法，它向用户发出个性化的问候。

#创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。

class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0

    def describe_user(self):
        print("这位用户是"+self.first_name.title()+" "+self.last_name.title())
    
    def greet_user(self):
        print("hello "+self.first_name.title()+" "+self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts+=1
    
    def reset_login_attempts(self):
        self.login_attempts=0

user=User("周","杰伦")
user1=User("许","嵩")
user.describe_user()
user.greet_user()
user1.describe_user()
user1.greet_user()

# 9-5 尝试登录次数：在为完成练习9-3而编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法，它将属性login_attempts的值加1。
# 再编写一个名为reset_login_attempts()的方法，它将属性login_attempts的值重置为0。
# 根据User类创建一个实例，再调用方法increment_login_attempts()多次。
# 打印属性login_attempts的值，确认它被正确地递增；然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。
    
user=User("周","杰伦")
user.increment_login_attempts()
print("重试次数: "+str(user.login_attempts))
user.increment_login_attempts()
print("重试次数: "+str(user.login_attempts))
user.increment_login_attempts()
print("重试次数: "+str(user.login_attempts))
user.reset_login_attempts()
print("重试次数: "+str(user.login_attempts))


# 9-7 管理员：管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习9-3或练习9-5而编写的User类。
# 添加一个名为privileges的属性，用于存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
# 编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。
# 9-8 权限：编写一个名为Privileges的类，它只有一个属性——privileges，其中存储了练习9-7所说的字符串列表。
# 将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。
# 创建一个Admin实例，并使用方法show_privileges()来显示其权限。

# class Privileges():
#     def __init__(self):
#         self.privileges=["can add post","can delete post","can ban user"]

#     def show_privileges(self):
#         print(self.privileges)

# class Admin(User):
    
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)
#         self.privileges=Privileges()



# admin=Admin("林","俊杰")
# admin.privileges.show_privileges()

