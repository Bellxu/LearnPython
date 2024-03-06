from random import randint
class Die:
    """""一个表示骰子的类"""
    def __init__(self,number_side = 6) -> None:
        """""骰子的面数"""
        self.number_side=number_side
        
    
    def roll(self):
        return(randint(1,self.number_side))