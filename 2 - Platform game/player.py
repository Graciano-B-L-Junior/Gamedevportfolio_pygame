import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.jump_force = 50
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 0, 0)

        self.__gravity = 1.5

        self.jumping = False
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_SPACE]:
            if not self.jumping:
                self.jumping = True

                self.y += -(self.speed * self.jump_force)

        self.y += self.__gravity

        self.rect.x = self.x
        self.rect.y = self.y