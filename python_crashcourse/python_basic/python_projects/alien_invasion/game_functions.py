import sys

import pygame

from python_crashcourse.python_basic.python_projects.alien_invasion import ship


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.key == pygame.K_UP:
            check_keyup_events(event, ship)




def update_screen(ai_settings, screen, ship, aliens):
    """Update the screen with the current state."""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
def check_keydown_events(event, ship):
    """Respond to keypresses and mouse events."""
    if event.key == pygame.K_RIGHT:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True

def check_keyup_events(event, ship):
    """Respond to keypresses and mouse events."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False