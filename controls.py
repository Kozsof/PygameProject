import pygame, sys, time
from bullet import Bullet
from ino import Ino
from menu import Menu
from scores import Scores


def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # кнопка вправо
            if event.key == pygame.K_RIGHT:
                gun.move_right = True
            # кнопка влево
            if event.key == pygame.K_LEFT:
                gun.move_left = True

            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # кнопка вправо
            if event.key == pygame.K_RIGHT:
                gun.move_right = False
            # кнопка влево
            if event.key == pygame.K_LEFT:
                gun.move_left = False


def update(back_ground_color, screen, stats, score, gun, inos, bullets):
    """Обновление экрана"""
    screen.fill(back_ground_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(stats, screen, score, gun, inos, bullets):
    """Обновляем пазиции пуль, чтобы они удалялись после выхода за контур"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 1 * len(inos)
        score.image_score()
        chack_hight_score(stats, score)
        score.image_life()
    if len(inos) == 0:
        bullets.empty()
        army(screen, inos)


def gun_kill(stats, screen, score, gun, inos, bullets):
    """Столкновение пушки и армии"""
    if stats.guns_life > 0:
        stats.guns_life -= 1
        score.image_life()
        inos.empty()
        bullets.empty()
        army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        game_over(score, stats)


def update_army(stats, screen, score, gun, inos, bullets):
    """Обновляем позицию армии"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, score, gun, inos, bullets)
    inos_came(stats, screen, score, gun, inos, bullets)


def inos_came(stats, screen, score, gun, inos, bullets):
    """Добрались ли пришельцы по конца экрана"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, score, gun, inos, bullets)
            break


def army(screen, inos):
    ino = Ino(screen)
    screen_rect = screen.get_rect()
    screen_width = screen_rect.width
    screen_height = screen_rect.height
    ino_width = ino.rect.width - 6
    ino_height = ino.rect.height
    count_ino_x = int((screen_width - 2 * ino_width) / ino_width)
    count_ino_y = int((screen_height - 50 - ino_height) / ino_height) - 10

    for row_ino in range(count_ino_y):
        for count_ino in range(count_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * count_ino
            ino.y = ino_height + ino_height * row_ino
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_ino
            inos.add(ino)


def chack_hight_score(stats, score):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.image_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(str(stats.high_score))


def game_over(score, stats):
    """создаем экран"""
    pygame.init()
    screen_width = 500
    screen_height = 650
    image = pygame.image.load("game_over.png").convert()
    ar = pygame.font.SysFont("ar", 80)
    screen = pygame.display.set_mode((screen_width, screen_height))
    back_ground_color = (0, 0, 0)
    menu = Menu()
    clock = pygame.time.Clock()
    menu.append_option("Выйти", quit, ar)

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
        screen.blit(image, (0, 50))
        score.show_final_score()
        menu.draw(screen, 170, 500, 100)
        pygame.display.flip()
        clock.tick(50)
