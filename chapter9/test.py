# 9-10 导入Restaurant类：将最新的Restaurant类存储在一个模块中。
# 在另一个文件中，导入Restaurant类，创建一个Restaurant实例，并调用Restaurant的一个方法，以确认import语句正确无误。
from restaurant import Reataurant

restaurant =Reataurant("麦当劳","美食快餐")
restaurant1 =Reataurant("KFC","美食快餐")
restaurant2 =Reataurant("蒸功夫","中式快餐")
print(restaurant.reataurant_name+"---"+restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

from admin import Admin

admin=Admin("周","杰伦")
admin.privileges.show_privileges()