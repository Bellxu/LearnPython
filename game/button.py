
import pygame.ftfont
from pygame.surface import Surface
class Button:
    def __init__(self,screen:Surface,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        #按钮的属性
        self.width,self.heght=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        #创建按钮的rect对象并使其居中
        self.rect=pygame.Rect(0,0,self.width,self.heght)
        self.rect.center=self.screen_rect.center
        #按钮的标签只需要创建一次
        self.prep_msg(msg)
    
    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)