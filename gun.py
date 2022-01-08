import pygame

class Gun:

    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load("gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):
        """рисуем Пушку"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиций пушки"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 1.5

        if self.move_left and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        self.center = self.screen_rect.centerx
