# 9-1 餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
class Reataurant():
    def __init__(self,reataurant_name,cuisine_type):
        self.reataurant_name=reataurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    
    def describe_restaurant(self):
        print("这间餐厅叫"+self.reataurant_name+"做菜类型是"+self.cuisine_type)

    def open_restaurant(self):
        print("餐厅正在营业")

    def set_number_served(self,number_served):
        self.number_served=number_served
    
    def increment_number_served(self,increment_number_served):
        self.number_served+=increment_number_served

# restaurant =Reataurant("麦当劳","美食快餐")
# restaurant1 =Reataurant("KFC","美食快餐")
# restaurant2 =Reataurant("蒸功夫","中式快餐")
# print(restaurant.reataurant_name+"---"+restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()

# 9-4 就餐人数：在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

restaurant=Reataurant("沙县小吃","中国小吃")
print("就餐人数: "+str(restaurant.number_served))
restaurant.number_served=10
print("就餐人数: "+str(restaurant.number_served))
restaurant.set_number_served(100)
print("就餐人数: "+str(restaurant.number_served))
restaurant.increment_number_served(10)
print("就餐人数: "+str(restaurant.number_served))


# 9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。
# 编写一个名为IceCreamStand的类，让它继承你为完成练习9-1或练习9-4而编写的Restaurant类。
# 这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。
# 添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。
class IceCreamStand(Reataurant):
    def __init__(self, reataurant_name, cuisine_type):
        super().__init__(reataurant_name, cuisine_type)
        self.flavors=["草莓","巧克力","香草"]

    def show_flacors(self):
        print(self.flavors)

iceCreamStand=IceCreamStand("哈根达斯","美国冰激凌")
iceCreamStand.show_flacors()