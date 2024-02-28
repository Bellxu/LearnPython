import sys
import pygame
from bullet import Bullet
from alien import Alien
from settings import Settings
from pygame.sprite import Group 
from ship import Ship
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import ScoreBoard



def check_events(settings,game_stats,screen,ship,aliens,bullets,play_button,score_board:ScoreBoard):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          check_key_down(event,settings,screen,ship,bullets)          
        elif event.type == pygame.KEYUP:
          check_key_up(event,ship)
        elif event.type ==pygame.MOUSEBUTTONDOWN:
           mouse_x,mouse_y=pygame.mouse.get_pos()
           check_play_button(settings,game_stats,screen,mouse_x,mouse_y,play_button,ship,bullets,aliens,score_board)

def check_play_button(settings,game_stats,screen,mouse_x,mouse_y,play_button:Button,ship:Ship,bullets:Group,aliens:Group,score_board:ScoreBoard):
   button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
   if button_clicked and not game_stats.game_activte :
      settings.initialize_dynamic_settings()
      pygame.mouse.set_visible(False)
      game_stats.rest_stats()
      game_stats.game_activte=True
      score_board.prep_score()
      score_board.prep_game_level()
      score_board.prep_high_score()
      score_board.prep_ships()
      #清空飞船子弹,飞船重新居中,创建新的外星人
      bullets.empty()
      aliens.empty()
      ship.center_ship()
      create_fleet(settings,screen,ship,aliens)
      
      


def check_key_down(event,settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
     ship.moving_right=True
    if event.key == pygame.K_LEFT:
     ship.moving_left=True
    if event.key == pygame.K_SPACE:
       fire_bullets(settings,screen,ship,bullets)
    if event.key ==pygame.K_ESCAPE:
       sys.exit()

def check_key_up(event,ship):
    if event.key == pygame.K_RIGHT:
     ship.moving_right=False
    if event.key == pygame.K_LEFT:
     ship.moving_left=False      


def update_screen(settings,screen,ship,aliens,bullets,game_stats,play_button,score_board):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    score_board.show_score()
    if not game_stats.game_activte:
       play_button.draw_button()
    pygame.display.flip()

def update_bullets(settings:Settings,screen,stats,score_board,ship:Ship,aliens:Group,bullets:Group): 
   bullets.update()
   for bullet in bullets.copy():
      if bullet.rect.bottom <= 0:
        bullets.remove(bullet)
   check_bullet_aline_collision(settings,screen,stats,score_board,ship,aliens,bullets)


def check_bullet_aline_collision(settings:Settings,screen,stats:GameStats,score_board:ScoreBoard,ship,aliens,bullets):
   collisions = pygame.sprite.groupcollide(aliens,bullets,True,True)
   if collisions:
      #一次循环内可能会有多个外星人被子弹打中
      for aliens in collisions.values():
         stats.score +=settings.aline_point *len(aliens)
         score_board.prep_score()
      check_high_score(stats,score_board)
   if len(aliens) == 0:
      bullets.empty()
      stats.game_level+=1
      score_board.prep_game_level()
      settings.increase_speed()
      create_fleet(settings,screen,ship,aliens)

def check_high_score(stats:GameStats,score_board:ScoreBoard):
   """""检查最高分有无需要更新"""
   if stats.score > stats.high_score:
      stats.high_score=stats.score
      score_board.prep_high_score()

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

def update_aliens(aliens,ship,bullets,score_board,settings,game_stats,screen):
  #  检查外星人是否超出屏幕
   check_fleet_edges(aliens,settings)
   aliens.update()
   # 检查外星人和飞船碰撞
   if pygame.sprite.spritecollideany(ship,aliens) : 
      ship_hit(aliens,ship,bullets,score_board,settings,game_stats,screen)
   check_aliens_bottom(aliens,ship,bullets,score_board,settings,game_stats,screen)

def check_aliens_bottom(aliens,ship,bullets,score_board,settings,game_stats,screen):
   """""检查外星人是不是碰到屏幕底部了"""
   for aline in aliens.sprites():
      if aline.rect.bottom >= screen.get_rect().bottom:
         ship_hit(aliens,ship,bullets,score_board,settings,game_stats,screen)
         break

def ship_hit(aliens:Group,ship:Ship,bullets:Group,score_board:ScoreBoard,settings:Settings,game_stats:GameStats,screen):
   """""响应外星人撞到飞船关系"""
   #飞船的命减去一条,外星人重置,子弹清空
   if game_stats.ship_left>0:
      game_stats.ship_left -=1
      score_board.prep_ships()
   else:
      game_stats.game_activte=False
      pygame.mouse.set_visible(True)
      
      aliens.empty()
      bullets.empty()
      create_fleet(settings,screen,ship,aliens)
      ship.center_ship()
      sleep(0.5)
   
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