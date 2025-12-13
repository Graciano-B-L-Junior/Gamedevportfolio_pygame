import pygame
from player import Player
from coin import Coin
from ui import UI


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
        self.ui = UI(game=self)

        self.clock = pygame.time.Clock()
        self.running = True
        self.platforms = [
            
        ]

        
        self.TILEMAP = [
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
            [1, 1, 1, 1, 1, 0, 3, 2, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        self.TILE_SIZE = self.screen_height // len(self.TILEMAP)
        self.coins = []
        self.load_map()

        self.player = Player(2 * self.TILE_SIZE, 5 * self.TILE_SIZE, self.screen_width)

        self.cam_offset_x = 0
        self.cam_offset_y = 0

        self.target_cam_x = 0
        self.cam_smoothing = 5 # Fator de suavização. Quanto maior, mais rápido a câmera segue.
        self.last_cam_offset_x = 0
        self.cam_offset_x_range = self.TILE_SIZE * 2

        self.MAP_HEIGHT_PIXELS = len(self.TILEMAP) * self.TILE_SIZE
        self.MAP_WIDTH_PIXELS = len(self.TILEMAP[0]) * self.TILE_SIZE

    def load_map(self):
        self.platforms = []
        self.coins = []
        for y_map, line in enumerate(self.TILEMAP):
            for x_map, tile in enumerate(line):
                pos_x = x_map * self.TILE_SIZE
                pos_y = y_map * self.TILE_SIZE
                if tile == 3:
                    self.coins.append(Coin(pos_x, pos_y))

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self,delta_time):
        self.platforms = []
        for y_map, line in enumerate(self.TILEMAP):
            for x_map, tile in enumerate(line):
                pos_x_world = x_map * self.TILE_SIZE
                pos_y_world = y_map * self.TILE_SIZE
                pos_x_screen = pos_x_world - self.cam_offset_x

                if tile in [1, 2] and -self.TILE_SIZE < pos_x_screen < self.screen_width:
                    rect = pygame.Rect(pos_x_screen, pos_y_world, self.TILE_SIZE, self.TILE_SIZE)
                    self.platforms.append((rect,tile))

        self.target_cam_x = self.player.rect.centerx - self.screen_width // 2

        self.cam_offset_x += (self.target_cam_x - self.cam_offset_x) * self.cam_smoothing * delta_time

        self.cam_offset_x = max(0, min(self.cam_offset_x, self.MAP_WIDTH_PIXELS - self.screen_width))
        
        self.difference = self.cam_offset_x - self.last_cam_offset_x
        
        self.last_cam_offset_x = self.cam_offset_x
        self.player.update(
            other_rects=self.platforms,
            delta_time=delta_time,
            offset_x=self.difference
        )
        
        for coin in self.coins:
            coin.update(self.player)
            if coin.collected:
                self.coins.remove(coin)



    def draw(self):
        self.screen.fill((135, 206, 235))

        for tuples in self.platforms:
            platform_rect = tuples[0]
            tile_type = tuples[1]
            draw_rect = platform_rect
            
            if  tile_type == 1:
                pygame.draw.rect(self.screen, self.GROUND_EARTH, draw_rect)
            else:
                pygame.draw.rect(self.screen, self.GREEN_GROUND, draw_rect)

        for coin in self.coins:
            coin.draw(self.screen, self.cam_offset_x)

        self.player.draw(self.screen)
        self.ui.draw(self.screen)

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
