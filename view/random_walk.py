from random import choice
class RandomWalk:
    """""一个生成随机漫步数据的类"""
    def __init__(self,number_points=5000):
        """""初始化随机漫步数据"""
        self.number_points = number_points
        
        self.x_vaules = [0]
        self.y_vaules = [0]
        
    def fill_walk(self):
        """""不断漫步直到满足个数"""
        
        while len(self.x_vaules) < self.number_points:
            #决定方向和距离
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step=x_direction * x_distance
            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_step=y_direction * y_distance
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #计算下个点的x,y
            x_next = self.x_vaules[-1] + x_step
            y_next = self.y_vaules[-1] + y_step
            self.x_vaules.append(x_next)
            self.y_vaules.append(y_next)