import pygame
from Physics.physics import PhysicsEngine

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


    def draw(self,win):
        pygame.draw.rect(win,self.color_brown,self.rect)

    def update(self,delta_time, other_rects=None, offset_x=0):
        super().update(delta_time)
        self.rect.x = self.get_x()
        self.rect.y = self.get_y()
        if other_rects and isinstance(other_rects,list):
            self.set_other_rects(other_rects)


    def set_other_rects(self,other_rects):
        self.other_rects = other_rects