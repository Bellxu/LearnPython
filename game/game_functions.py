import sys
import pygame
from bullet import Bullet
from alien import Alien
from settings import Settings
from pygame.sprite import Group 



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

def update_bullets(bullets): 
    bullets.update()
    for bullet in bullets.copy():
      if bullet.rect.bottom <= 0:
        bullets.remove(bullet)

def fire_bullets(settings,screen,ship,bullets):
    if len(bullets) < settings.bullets_allowed:
      new_bullet=Bullet(settings,screen,ship)
      bullets.add(new_bullet)

def create_fleet(settings:Settings,screen,aliens:Group):
   """"创建外星人群"""
   #创建一个外星人并计算一行能容纳多少个
   #外星人间距为外星人宽度
   alien=Alien(settings,screen)
   alien_width=alien.rect.width
   #屏幕宽度两边留出一个外星人的宽度间距
   available_space_x=settings.screen_width-2*alien_width
   #每个外星人直接留宽度一半的间距
   allowed_alien_number=int(available_space_x/(2*alien_width))
   #创建第一行外星
   for alien_number in range(allowed_alien_number):
      #创建一个外星人并加入当前行
      alien=Alien(settings,screen)
      #间隔一个+一个横坐标
      alien.x = alien_width + 2*alien_width * alien_number
      alien.rect.x=alien.x
      aliens.add(alien)