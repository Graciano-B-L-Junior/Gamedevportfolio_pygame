import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.jump_force = -20
        self.maximum_fall_speed = 10
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 0, 0)

        self.y_velocity = 0
        self.gravity = 1
        self.on_ground = False
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, other_rects):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        for platform in other_rects:
            if self.rect.colliderect(platform):
                if self.rect.right > platform.left and self.rect.left < platform.left:
                    self.rect.right = platform.left
                elif self.rect.left < platform.right and self.rect.right > platform.right:
                    self.rect.left = platform.right

        if keys[pygame.K_SPACE] and self.on_ground:
            self.y_velocity = self.jump_force
            self.on_ground = False
        
        self.y_velocity += self.gravity
        self.y_velocity = min(self.y_velocity, self.maximum_fall_speed)
        self.rect.y += self.y_velocity
        
        self.on_ground = False
        for platform in other_rects:
            if self.rect.colliderect(platform):
                if self.y_velocity > 0:
                    self.rect.bottom = platform.top
                    self.y_velocity = 0
                    self.on_ground = True
                elif self.y_velocity < 0:
                    self.rect.top = platform.bottom
                    self.y_velocity = 0

        self.x = self.rect.x
        self.y = self.rect.y

            