import pygame
from player import Player

class PhysicsEngine:
    def __init__(self):
        self.x=0
        self.y=0
        self.vx=0
        self.vy=0
        self.gravity = 100
        self.other_rects = []


    def update(self,delta_time):
        self.vy += self.gravity * delta_time
        for rect in self.other_rects:
            self.collision(rect)
            
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time



    def collision(self, other):
        self.rect = self.get_rect()
        if isinstance(other, Player):
            other = other.rect
        
        if hasattr(self, 'rect'):
            if self.rect.colliderect(other):
                if self.vx > 0:
                    if self.rect.right > other.left and self.rect.left < other.right:
                        self.rect.right = other.left
                        self.vx = 0
                elif self.vx < 0:
                    if self.rect.left < other.right and self.rect.right > other.left:
                        self.rect.left = other.right
                        self.vx = 0

                if self.vy > 0:
                    if self.rect.bottom > other.top and self.rect.top < other.bottom:
                        self.rect.bottom = other.top
                        self.vy = 0
                elif self.vy < 0:
                    if self.rect.top < other.bottom and self.rect.bottom > other.top:
                        self.rect.top = other.bottom
                        self.vy = 0
        else:
            raise Exception(f"{__class__} doesn't have 'rect' attribute")
    

    def update_vx(self, vx):
        self.vx = vx

    def update_vy(self, vy):
        self.vy = vy

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_vx(self):
        return self.vx

    def get_vy(self):
        return self.vy

    def get_gravity(self):
        return self.gravity

    def set_gravity(self, gravity):
        self.gravity = gravity
    
    def get_rect(self):
        return self.rect
