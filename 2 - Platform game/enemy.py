import pygame
from Physics.physics import PhysicsEngine

class Enemy(PhysicsEngine):
    def __init__(self,x,y,width,height):
        super().__init__()

        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.color_brown = (165, 42, 42)
        self.rect = pygame.Rect(self.pos_x,self.pos_y,self.width,self.height)
        self.other_rects = []


    def draw(self,win,other_rects=None):
        pygame.draw.rect(win,self.color_brown,self.rect)

    def update(self,delta_time):
        super().update(delta_time)
        self.rect.x = self.get_x()
        self.rect.y = self.get_y()

    def set_other_rects(self,other_rects):
        self.other_rects = other_rects