import pygame

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 255, 0)
        self.collected = False

    def draw(self, surface, offset_x=0):
        if not self.collected:
            draw_rect = self.rect.copy()
            draw_rect.x -= offset_x
            pygame.draw.rect(surface, self.color, draw_rect)

    def update(self, player):
        if not self.collected and self.rect.colliderect(player.rect):
            self.collected = True
            player.update_collected_coins(1)