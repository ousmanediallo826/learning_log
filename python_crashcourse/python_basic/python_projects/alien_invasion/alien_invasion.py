
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    pygame.display.set_caption('Alien Invasion')
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.fill(ai_settings.bg_color)

    #Make a Ship
    ship = Ship(ai_settings, screen)

    gf.check_events(ship)

    while True:
        ship.blitme()
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()