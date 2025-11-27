import pygame
import random
import os

HEIGH_SPACE = 200
HEIGHT = 800


class Pipe:
    def __init__(self, x):

        self.pos_x = x
        self.passed = False
        self.width = 70

        script_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(script_dir, 'assets')
        pipe_img_path = os.path.join(assets_dir, 'pipe.png')

        center_space_y = random.randint(HEIGH_SPACE, HEIGHT - HEIGH_SPACE)
        self.top_pipe_rect = pygame.Rect(
            self.pos_x, 0, self.width, center_space_y-HEIGH_SPACE 
        )

        self.bottom_pipe_rect = pygame.Rect(
            self.pos_x, center_space_y + HEIGH_SPACE, self.width, HEIGHT - (center_space_y + HEIGH_SPACE)
        )

        self.pipe_img = pygame.image.load(pipe_img_path).convert_alpha()
        self.top_pipe_img = pygame.transform.scale(self.pipe_img, (self.width, center_space_y-HEIGH_SPACE))
        self.top_pipe_img = pygame.transform.rotate(self.top_pipe_img, 180)

        self.bottom_pipe_img = pygame.transform.scale(
            self.pipe_img, 
            (self.width, HEIGHT - (center_space_y + HEIGH_SPACE))
        )

    def draw(self, screen):
        screen.blit(self.top_pipe_img, self.top_pipe_rect)
        screen.blit(self.bottom_pipe_img, self.bottom_pipe_rect)


    def move(self):
        self.pos_x -= 4
        self.top_pipe_rect.x = self.pos_x
        self.bottom_pipe_rect.x = self.pos_x

    def check_collision(self, bird_rect):
        if self.top_pipe_rect.colliderect(bird_rect) or self.bottom_pipe_rect.colliderect(bird_rect):
            return True
        else:
            return False


