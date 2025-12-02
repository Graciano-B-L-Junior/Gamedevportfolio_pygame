import pygame
from player import Player

class Game:

    GROUND_EARTH = (139, 69, 19) 
    GREEN_GROUND = (0, 150, 0)
    WHITE = (255, 255, 255)



    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("2D Platformer")

        self.clock = pygame.time.Clock()
        self.running = True
        self.platforms = [
        ]

        self.TILE_SIZE = 32
        self.TILEMAP = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        self.player = Player(2 * self.TILE_SIZE, 5 * self.TILE_SIZE, self.screen_width)

        self.cam_offset_x = 0
        self.cam_offset_y = 0

        self.target_cam_x = 0
        self.last_cam_offset_x = 0
        self.cam_offset_x_range = self.TILE_SIZE * 2

        self.MAP_HEIGHT_PIXELS = len(self.TILEMAP) * self.TILE_SIZE
        self.MAP_WIDTH_PIXELS = len(self.TILEMAP[0]) * self.TILE_SIZE
    


    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.target_cam_x = self.player.rect.x - self.screen_width // 2
        if self.target_cam_x < 0:
            self.cam_offset_x = 0
        elif self.target_cam_x > self.MAP_WIDTH_PIXELS - self.screen_width:
            self.cam_offset_x = self.MAP_WIDTH_PIXELS - self.screen_width
        else:
            self.cam_offset_x = self.target_cam_x
        
        cam_is_moving = False

        if self.last_cam_offset_x + self.cam_offset_x_range //2 < self.cam_offset_x:
            cam_is_moving = True
        elif self.last_cam_offset_x - self.cam_offset_x_range //2 > self.cam_offset_x:
            cam_is_moving = True
        
        self.player.update(
            self.platforms, 
            cam_offset_x=self.cam_offset_x, 
            cam_is_moving=cam_is_moving
        )

        self.last_cam_offset_x = self.cam_offset_x

    def draw(self):
        self.screen.fill((135, 206, 235))
        self.player.draw(self.screen)
        self.platforms=[]
        for y_map, line in enumerate(self.TILEMAP):
            for x_map, tile in enumerate(line):

                pos_x_world = x_map * self.TILE_SIZE
                pos_y_world = y_map * self.TILE_SIZE

                pos_x_screen = pos_x_world - self.cam_offset_x
                rect = None
                if pos_x_screen + self.TILE_SIZE > 0 and pos_x_screen < self.screen_width:
                    if tile == 1:
                       rect = pygame.draw.rect(self.screen, self.GROUND_EARTH, (pos_x_screen, pos_y_world, self.TILE_SIZE, self.TILE_SIZE))
                    elif tile == 2:
                        rect =pygame.draw.rect(self.screen, self.GREEN_GROUND, (pos_x_screen, pos_y_world, self.TILE_SIZE, self.TILE_SIZE))
                if rect:
                    self.platforms.append(rect)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
