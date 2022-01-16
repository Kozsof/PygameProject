import pygame

class Menu:
    def __init__(self):
        self.op_surf = []
        self.call_backs = []
        self.opt_ind = 0

    def append_option(self, option, callback, ar):
        self.op_surf.append(ar.render(option, True, (255, 255, 255)))
        self.call_backs.append(callback)

    def switch(self, direction):
        self.opt_ind = max(0, min(self.opt_ind + direction, len(self.op_surf) - 1))

    def select(self):
        self.call_backs[self.opt_ind]()

    def draw(self, screen, x, y, ots):
        for i, op in enumerate(self.op_surf):
            op_rect = op.get_rect()
            op_rect.topleft = (x, y + i * ots)
            if i == self.opt_ind:
                pygame.draw.rect(screen, (0, 150, 0), op_rect)
            screen.blit(op, op_rect)
