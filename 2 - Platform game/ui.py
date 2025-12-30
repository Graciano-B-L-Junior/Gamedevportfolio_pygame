import pygame

class UI:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 30)

    def draw(self, surface):
        coin_count_text = self.font.render(f"Coins: {self.game.player.coins_collected}", True, self.game.WHITE)
        player_health = self.font.render(f"Health: {self.game.player.health}", True, self.game.WHITE)
        surface.blit(coin_count_text, (10, 10))
        surface.blit(player_health, (10, 40))

class UI_GameOver(UI):

    def draw(self, surface):
        game_over_text = self.font.render("Game Over! Press R to restart", True, self.game.WHITE)
        surface.blit(game_over_text, (self.game.screen_width // 2 - game_over_text.get_width() // 2, 
                                      self.game.screen_height // 2 - game_over_text.get_height() // 2)
                    )


class UI_Win(UI):

    def draw(self, surface):
        win_text = self.font.render("You Win! Press R to restart", True, self.game.WHITE)
        surface.blit(win_text, (self.game.screen_width // 2 - win_text.get_width() // 2, 
                                      self.game.screen_height // 2 - win_text.get_height() // 2)
                    )