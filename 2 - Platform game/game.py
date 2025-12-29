import pygame
from player import Player
from coin import Coin
from ui import UI, UI_GameOver, UI_Win
from enemy import Enemy

TILEMAP = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 3, 2, 2, 2, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Game:
    GROUND_EARTH = (139, 69, 19) 
    GREEN_GROUND = (0, 150, 0)
    WHITE = (255, 255, 255)

    def __init__(self):
        pygame.init()
        self.screen_width = 900
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("2D Platformer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.TILE_SIZE = self.screen_height // len(TILEMAP)
        # Game Objects
        self.player = None
        self.enemies = []
        self.ui = None
        self.ui_game_over = None
        self.ui_win = None
        self.platforms = [] # List of (rect, tile_type)
        self.platform_rects = [] # List of rects only, for collision
        self.coins = []
        self.coins_length = None
        self._create_entities()
        self.trigger = False
        # Camera
        self.cam_offset_x = 0
        self.target_cam_x = 0
        self.cam_smoothing = 5 # Fator de suavização. Quanto maior, mais rápido a câmera segue.
        self.last_cam_offset_x = 0
        self.difference = 0

        self.MAP_WIDTH_PIXELS = len(TILEMAP[0]) * self.TILE_SIZE

    def _create_entities(self):
        self.load_map()
        world_x_size = len(TILEMAP[0]) * self.TILE_SIZE

        self.player = Player(2 * self.TILE_SIZE, 5 * self.TILE_SIZE, world_x_size)
        self.ui = UI(game=self)
        self.ui_game_over = UI_GameOver(game=self)
        self.ui_win = UI_Win(game=self)

    def load_map(self):
        self.platforms = []
        self.coins = []
        self.enemies = []
        for y_map, line in enumerate(TILEMAP):
            for x_map, tile in enumerate(line):
                pos_x_world = x_map * self.TILE_SIZE
                pos_y_world = y_map * self.TILE_SIZE
                if tile == 3:
                    self.coins.append(Coin(pos_x_world, pos_y_world))
                elif tile in [1, 2]:
                    rect = pygame.Rect(pos_x_world, pos_y_world, self.TILE_SIZE, self.TILE_SIZE)
                    self.platforms.append((rect, tile))
                elif tile == 4:
                    self.enemies.append(Enemy(pos_x_world, pos_y_world, self.TILE_SIZE, self.TILE_SIZE))
        self.coins_length = len(self.coins)
        self.platform_rects = [p[0] for p in self.platforms]

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and (self.player.coins_collected == self.coins_length or self.player.player_dead()):
                    self._create_entities()
                    self.cam_offset_x = 0
                    self.target_cam_x = 0
                    self.last_cam_offset_x = 0
                    self.difference = 0

    def _update_camera(self, delta_time):
        self.target_cam_x = self.player.rect.centerx - self.screen_width // 2
        self.cam_offset_x += (self.target_cam_x - self.cam_offset_x) * self.cam_smoothing * delta_time
        self.cam_offset_x = max(0, min(self.cam_offset_x, self.MAP_WIDTH_PIXELS - self.screen_width))
        
        self.difference = self.cam_offset_x - self.last_cam_offset_x
        self.last_cam_offset_x = self.cam_offset_x

    def _update_entities(self, delta_time):
        self.player.update(
            other_rects=self.platform_rects,
            delta_time=delta_time,
            offset_x=self.difference
        )

        for coin in self.coins[:]:
            coin.update(self.player)
            if coin.collected:
                self.coins.remove(coin)

        collidables = [*self.platform_rects, self.player]
        for enemy in self.enemies[:]:
            enemy.update(
                delta_time,
                other_rects=collidables,
                offset_x=self.difference
            )
            if enemy.is_dead:
                self.enemies.remove(enemy)

    def update(self, delta_time):
        self._update_camera(delta_time)
        self._update_entities(delta_time)

    def draw(self):
        self.screen.fill((135, 206, 235))
        # Draw level geometry
        for platform_rect, tile_type in self.platforms:
            draw_rect = platform_rect.copy()
            draw_rect.x -= self.cam_offset_x
            
            if draw_rect.right > 0 and draw_rect.left < self.screen_width:
                color = self.GROUND_EARTH if tile_type == 1 else self.GREEN_GROUND
                pygame.draw.rect(self.screen, color, draw_rect)

        # Draw entities
        for coin in self.coins:
            coin.draw(self.screen, self.cam_offset_x)

        self.player.draw(self.screen, self.cam_offset_x)
        for enemy in self.enemies:
            enemy.draw(self.screen, self.cam_offset_x)
        self.ui.draw(self.screen)

        if self.player.player_dead():
            self.ui_game_over.draw(self.screen)
        elif self.player.coins_collected == self.coins_length:
            self.ui_win.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running: 
            delta_time = self.clock.get_time() / 1000.0
            self.handle_input()
            self.update(delta_time=delta_time)
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        

if __name__ == "__main__":
    game = Game()
    game.run()
