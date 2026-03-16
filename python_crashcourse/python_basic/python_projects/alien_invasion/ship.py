import pygame

class Ship():
    def __init__(self,ai_settings,  screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        # 1. Load the original image
        original_image = pygame.image.load('./images/alien-1.bmp')

        # 2. Scale it (e.g., to 50x50 pixels)
        self.image = pygame.transform.scale(original_image, (50, 50))

        # 3. Get the rect from the NEW scaled image
        self.rect = self.image.get_rect()

        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom
    def update(self):
        if self.moving_right and self.rect.right < self.screen.get_rect:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)