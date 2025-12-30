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
        self.health = 5
        self.vx = -50 # Start moving left


    def draw(self,win, offset_x=0):
        draw_rect = self.rect.copy()
        draw_rect.x -= offset_x
        pygame.draw.rect(win,self.color_brown,draw_rect)
        
    def update(self,delta_time, other_rects=None, offset_x=0):
        self.other_rects = other_rects
        super().update(delta_time)

    def handle_horizontal_collisions(self):
        player_instance = None
        for other in self.other_rects:
            is_player_instance = False
            if isinstance(other, Player):
                rect = other.rect
                is_player_instance = True
                player_instance = other
            else:
                rect = other
            if self.rect.colliderect(rect):
                if isinstance(other, Player) and rect.bottom < self.rect.centery:
                    continue
                elif self.rect.centerx < rect.centerx:
                    self.rect.right = rect.left
                else:
                    self.rect.left = rect.right

                if is_player_instance:
                    player_instance.get_hit_signal(self.rect)

                self.vx *= -1

    def handle_vertical_collisions(self):
        self.on_ground = False
        for rect in self.other_rects:
            is_player_instance = False
            if isinstance(rect, Player):
                is_player_instance = True
                player_instance = rect
                rect = rect.rect
            if self.rect.colliderect(rect):
                if is_player_instance:
                    self.health -= 1
                    player_instance.game.enemy_hurt_sfx()
                    player_instance.get_hit_signal(self.rect)
                elif self.vy > 0:  
                    self.rect.bottom = rect.top
                    self.on_ground = True
                    self.vy = 0
                elif self.vy < 0:
                    self.rect.top = rect.bottom
                    self.vy = 0

    @property
    def is_dead(self):
        return self.health <= 0