import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    """создаем экран"""
    pygame.init()
    screen_width = 500
    screen_height = 650
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game")
    back_ground_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.army(screen, inos)
    stats = Stats()
    score = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(back_ground_color, screen, stats, score, gun, inos, bullets)
            controls.update_bullets(stats, screen, score, gun, inos, bullets)
            controls.update_army(stats, screen, score, gun, inos, bullets)


run()
