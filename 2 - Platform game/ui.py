import pygame

class UI:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 30)

    def draw(self, surface):
        coin_count_text = self.font.render(f"Coins: {self.game.player.coins_collected}", True, self.game.WHITE)
        surface.blit(coin_count_text, (10, 10))
