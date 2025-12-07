import pygame

class Player:
    def __init__(self, x, y, game_screen):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.jump_force = -20
        self.maximum_fall_speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.last_position_rect = self.rect.copy()
        self.color = (255, 0, 0)
        self.dx = 0
        self.acceleration_rate = 1.5
        self.friction = 0.15
        self.y_velocity = 0
        self.gravity = 1
        self.on_ground = False
        self.is_jumping = False
        self.high_jump = -0.3

        self.screen_width = game_screen
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, other_rects, **kwargs):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.on_ground:
            self.y_velocity = self.jump_force
            self.on_ground = False
            self.is_jumping = True
        
        if self.is_jumping and keys[pygame.K_SPACE]:
            self.y_velocity += self.high_jump
        else:
            self.is_jumping = False

        if kwargs.get("cam_offset_x") and kwargs.get('cam_is_moving'):
            self.speed = 3
        else:
            self.speed = 5

        if keys[pygame.K_LEFT]:
            self.dx -= self.acceleration_rate
        elif keys[pygame.K_RIGHT]:
            self.dx += self.acceleration_rate
        else:
            if self.dx > 0:
                self.dx -= self.friction
                if self.dx < 0: self.dx = 0
            elif self.dx < 0:
                self.dx += self.friction
                if self.dx > 0: self.dx = 0

        if self.dx > self.speed:
            self.dx = self.speed
        if self.dx < -self.speed:
            self.dx = -self.speed

        self.rect.x += self.dx
        for platform in other_rects:
            platform = platform[0]
            if self.rect.colliderect(platform):
                if self.dx > 0:
                    self.rect.right = platform.left
                elif self.dx < 0:
                    self.rect.left = platform.right
                self.dx = 0

        self.y_velocity += self.gravity
        self.y_velocity = min(self.y_velocity, self.maximum_fall_speed) 

        self.rect.y += self.y_velocity
        self.on_ground = False
        for platform in other_rects:
            platform = platform[0]
            if self.rect.colliderect(platform):
                if self.y_velocity > 0:
                    self.rect.bottom = platform.top
                    self.y_velocity = 0
                    self.on_ground = True
                elif self.y_velocity < 0:
                    self.rect.top = platform.bottom
                    self.y_velocity = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0