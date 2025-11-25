import pygame
import random

HEIGH_SPACE = 200
HEIGHT = 800


class Pipe:
    def __init__(self, x):

        self.pos_x = x
        self.passed = False

        center_space_y = random.randint(HEIGH_SPACE, HEIGHT - HEIGH_SPACE)
        self.top_pipe_rect = pygame.Rect(
            self.pos_x, 0, 70, center_space_y-HEIGH_SPACE 
        )

        self.bottom_pipe_rect = pygame.Rect(
            self.pos_x, center_space_y + HEIGH_SPACE, 70, HEIGHT - (center_space_y + HEIGH_SPACE)
        )
        print(center_space_y)

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 255, 0), self.top_pipe_rect)
        pygame.draw.rect(screen, (100, 255, 0), self.bottom_pipe_rect)

    def move(self):
        self.pos_x -= 5
        self.top_pipe_rect.x = self.pos_x
        self.bottom_pipe_rect.x = self.pos_x
