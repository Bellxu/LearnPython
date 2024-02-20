import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          check_key_down(event,ship)          
        elif event.type == pygame.KEYUP:
          check_key_up(event,ship)


def check_key_down(event,ship):
    if event.key == pygame.K_RIGHT:
     ship.moving_right=True
    if event.key == pygame.K_LEFT:
     ship.moving_left=True

def check_key_up(event,ship):
    if event.key == pygame.K_RIGHT:
     ship.moving_right=False
    if event.key == pygame.K_LEFT:
     ship.moving_left=False      


def update_screen(settings,screen,ship):
     screen.fill(settings.bg_color)
     ship.blitme()
     pygame.display.flip()