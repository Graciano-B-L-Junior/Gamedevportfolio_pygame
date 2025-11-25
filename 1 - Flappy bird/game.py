import pygame
from pipe import Pipe

pygame.init()

WIDTH = 600
HEIGHT = 800

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird clone")

#colors

WHITE = (255, 255, 255)
BLUE_SKY = (113, 197, 207)

CLOCK = pygame.time.Clock()
FPS = 60
GRAVITY = 1.5
VELOCITY = -25

#game loop

bird_size = 30
bird_pos_x = WIDTH // 4
bird_pos_y = HEIGHT // 2
bird_rect = pygame.Rect(
    bird_pos_x, bird_pos_y, bird_size, bird_size
    )

pipe = Pipe(WIDTH)

running = True
velocity_y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                velocity_y = VELOCITY




    velocity_y += GRAVITY

    if velocity_y >10:
        velocity_y = 10
    
    bird_rect.y += velocity_y

    if bird_rect.bottom >= HEIGHT:
        bird_rect.bottom = HEIGHT
        velocity_y = 0
    elif bird_rect.top <= 0:
        bird_rect.top = 0
        velocity_y = 0
    
    pipe.move()

    SCREEN.fill(BLUE_SKY)
    pygame.draw.rect(SCREEN, WHITE, bird_rect)
    pipe.draw(SCREEN)
    pygame.display.flip()

    CLOCK.tick(FPS)

pygame.quit()
quit()