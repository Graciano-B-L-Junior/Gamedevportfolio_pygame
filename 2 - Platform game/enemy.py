import pygame
from Physics.physics import PhysicsEngine
from player import Player

class Enemy(PhysicsEngine):
    def __init__(self,x,y,width,height):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_brown = (165, 42, 42)
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.other_rects = []
        self.health = 2
        self.vx = -50 # Start moving left


    def draw(self,win, offset_x=0):
        draw_rect = self.rect.copy()
        draw_rect.x -= offset_x
        pygame.draw.rect(win,self.color_brown,draw_rect)
        
    def update(self,delta_time, other_rects=None, offset_x=0):
        # We only want to collide with platforms, not the player for movement
        platform_rects = [r for r in other_rects if not isinstance(r, Player) and not r == self.rect]
        self.other_rects = platform_rects
        super().update(delta_time)