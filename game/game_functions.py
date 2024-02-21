import sys
import pygame
from bullet import Bullet



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

def check_key_up(event,ship):
    if event.key == pygame.K_RIGHT:
     ship.moving_right=False
    if event.key == pygame.K_LEFT:
     ship.moving_left=False      


def update_screen(settings,screen,ship,bullets):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
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