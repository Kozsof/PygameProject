import pygame.font
from pygame.sprite import Sprite, Group


class Scores:
    """Вывод игровой информации"""

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 25)
        self.image_score()
        self.image_high_score()
        self.image_life()

    def image_score(self):
        self.score_image = self.font.render(f"New score <{str(self.stats.score)}>", True, self.text_color, "black")
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def image_high_score(self):
        self.high_score_image = self.font.render(f"High score <{str(self.stats.high_score)}>",
                                                 True, self.text_color, "black")
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def image_life(self):
        self.lives = Group()
        for count_life in range(self.stats.guns_life):
            life = Life(self.screen)
            life.rect.x = 15 + count_life * life.rect.width
            life.rect.y = 20
            self.lives.add(life)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lives.draw(self.screen)

    def show_final_score(self):
        self.font = pygame.font.SysFont("centuryschoolbook", 60)
        self.your_image = self.font.render(f"Your score", True, self.text_color, "black")
        self.your_rect = self.your_image.get_rect()
        self.your_rect.left = self.screen_rect.left + 130
        self.your_rect.top = 200

        self.score_image = self.font.render(f"< {str(self.stats.score)} >", True, self.text_color, "black")
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 200
        self.score_rect.top = 325
        self.screen.blit(self.your_image, self.your_rect)
        self.screen.blit(self.score_image, self.score_rect)


class Life(Sprite):
    def __init__(self, screen):
        super(Life, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("heart.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):
        """рисуем жизнь"""
        self.screen.blit(self.image, self.rect)
