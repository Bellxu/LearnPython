import pygame
from pygame.sprite import Group 
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button 
from scoreboard import ScoreBoard
def run_game():
    pygame.init()
    settings=Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    ship=Ship(screen,settings)
    game_stats=GameStats(settings)
    pygame.display.set_caption("Alien Invasion")
    bullets = Group()
    aliens = Group()
    play_button=Button(screen,"Play")
    score_board=ScoreBoard(screen,settings,game_stats)
    gf.create_fleet(settings,screen,ship,aliens)
    while True:
        gf.check_events(settings,game_stats,screen,ship,aliens,bullets,play_button)
        if game_stats.game_activte: 
            ship.update()
            gf.update_bullets(settings,screen,game_stats,score_board,ship,aliens,bullets)
            gf.update_aliens(aliens,ship,bullets,settings,game_stats,screen)
        gf.update_screen(settings,screen,ship,aliens,bullets,game_stats,play_button,score_board)
run_game()