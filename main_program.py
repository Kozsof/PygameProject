import pygame, controls, sys
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from menu import Menu



def load_image(name, color_key=None):
    try:
        image = pygame.image.load(name).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image



class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, all_sprites):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]



def start_screen():
    """создаем экран"""
    pygame.init()
    screen_width = 500
    screen_height = 650
    ar = pygame.font.SysFont("ar", 80)
    screen = pygame.display.set_mode((screen_width, screen_height))
    back_ground_color = (0, 0, 0)
    menu = Menu()
    clock = pygame.time.Clock()
    menu.append_option("Начать", lambda: print("start-->>"), ar)
    menu.append_option("Выйти", quit, ar)
    all_sprites = pygame.sprite.Group()
    image1 = pygame.image.load("images/uk.png").convert()
    image2 = pygame.image.load("images/uk2.png").convert()
    slime = pygame.image.load("images/slime.png").convert()
    slime2 = pygame.image.load("images/slime2.png").convert()
    planet = AnimatedSprite(load_image("images/planet.png", -1), 8, 8, 200, 300, all_sprites)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    menu.switch(1)
                if event.key == pygame.K_UP:
                    menu.switch(-1)
                if event.key == pygame.K_SPACE:
                    menu.select()
                    return

        screen.fill(back_ground_color)
        all_sprites.draw(screen)
        all_sprites.update()
        screen.blit(image2, (0, 0))
        screen.blit(slime, (10, 150))
        screen.blit(image1, (350, 500))
        screen.blit(slime2, (35, 440))
        menu.draw(screen, 160, 100, 100)
        pygame.display.flip()
        clock.tick(50)

def run():
    pygame.init()
    screen_width = 500
    screen_height = 650
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Invasion")
    icon = pygame.image.load("images/zast.png")
    pygame.display.set_icon(icon)
    back_ground_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.army(screen, inos)
    stats = Stats()
    score = Scores(screen, stats)

    start_screen()

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(back_ground_color, screen, stats, score, gun, inos, bullets)
            controls.update_bullets(stats, screen, score, gun, inos, bullets)
            controls.update_army(stats, screen, score, gun, inos, bullets)
run()
