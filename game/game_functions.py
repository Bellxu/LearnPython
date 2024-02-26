import sys
import pygame
from bullet import Bullet
from alien import Alien
from settings import Settings
from pygame.sprite import Group 
from ship import Ship



def check_events(settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          check_key_down(event,settings,screen,ship,bullets)          
        elif event.type == pygame.KEYUP:
          check_key_up(event,ship)


def check_key_down(event,settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
     ship.moving_right=True
    if event.key == pygame.K_LEFT:
     ship.moving_left=True
    if event.key == pygame.K_SPACE:
       fire_bullets(settings,screen,ship,bullets)
    if event.key ==pygame.K_k:
       sys.exit()

def check_key_up(event,ship):
    if event.key == pygame.K_RIGHT:
     ship.moving_right=False
    if event.key == pygame.K_LEFT:
     ship.moving_left=False      


def update_screen(settings,screen,ship,aliens,bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(bullets:Group,settings,screen,ship,aliens): 
    bullets.update()
    for bullet in bullets.copy():
      if bullet.rect.bottom <= 0:
        bullets.remove(bullet)
   # 如果有子弹和外星人有交错就移除
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    #如果外星人被消灭完了就创建新的
    if len(aliens) == 0:
       bullets.empty()
       create_fleet(settings,screen,ship,aliens)

def fire_bullets(settings,screen,ship,bullets):
    if len(bullets) < settings.bullets_allowed:
      new_bullet=Bullet(settings,screen,ship)
      bullets.add(new_bullet)

def get_alien_x_number(settings,alien_width):
   
   #屏幕宽度两边留出一个外星人的宽度间距
   available_space_x=settings.screen_width-2*alien_width
   #每个外星人直接留宽度一半的间距
   alien_x_number=int(available_space_x/(2*alien_width))
   return alien_x_number     

def get_alien_y_number(settings:Settings,alien_height,ship:Ship):
   """计算能容纳多少行"""
   #可用的高度应该是将屏幕高度减去第一行外星人的上边距（外星人高度）、飞船的高度以及最初外星人高度加上外星人间距（外星人高度的两倍）
   available_space_y=(settings.screen_height-(alien_height*4)-ship.rect.height)
   alien_y_number=int(available_space_y/(alien_height*2))
   return alien_y_number

def create_alien(settings,screen,alien_x_number_i,alien_y_number_i):
  alien=Alien(settings,screen)
  #间隔一个+一个横坐标
  alien_width=alien.rect.width
  alien_height=alien.rect.height
  alien.x = alien_width + 2*alien_width * alien_x_number_i
  alien.rect.x=alien.x
  alien.rect.y = alien_height + 2*alien_height * alien_y_number_i
  return alien
   
def create_fleet(settings:Settings,screen,ship:Ship,aliens:Group):
   """"创建外星人群"""
   #创建一个外星人并计算一行能容纳多少个
   #外星人间距为外星人宽度
   alien=Alien(settings,screen)
   alien_width=alien.rect.width
   alien_height=alien.rect.height
   alien_x_number=get_alien_x_number(settings,alien_width)
   alien_y_number=get_alien_y_number(settings,alien_height,ship)
   #创建第一行外星
   for alien_y_number_i in range(alien_y_number):
    for alien_x_number_i in range(alien_x_number):
      #创建一个外星人并加入当前行
      alien=create_alien(settings,screen,alien_x_number_i,alien_y_number_i)
      aliens.add(alien)

def update_aliens(aliens:Group,settings:Settings):
  #  检查外星人是否超出屏幕
   check_fleet_edges(aliens,settings)
   aliens.update()

def check_fleet_edges(aliens:Group,settings:Settings):
   for aline in aliens.sprites():
      if aline.check_edges():
        #  改变方向往下移移动
         changes_aliens_direction(aliens,settings)
         break

def changes_aliens_direction(aliens:Group,settings:Settings):
   for aline in aliens.sprites():
      aline.rect.y+=settings.alien_fleet_drop_speed
   settings.alien_fleet_direction *=-1