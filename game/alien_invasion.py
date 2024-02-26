import pygame
from pygame.sprite import Group 
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    settings=Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    ship=Ship(screen,settings)
    pygame.display.set_caption("Alien Invasion")
    bullets = Group()
    aliens = Group()
    gf.create_fleet(settings,screen,ship,aliens)
    while True:
        gf.check_events(settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets,settings,screen,ship,aliens)
        gf.update_aliens(aliens,settings)
        gf.update_screen(settings,screen,ship,aliens,bullets)
run_game()