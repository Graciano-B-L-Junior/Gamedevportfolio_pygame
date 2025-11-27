import sys, os
import pygame
from pipe import Pipe

pygame.init()

WIDTH = 600
HEIGHT = 800

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird clone")

#colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE_SKY = (113, 197, 207)

CLOCK = pygame.time.Clock()
FPS = 60
GRAVITY = 1.5
VELOCITY = -25

#game loop

bird_size = 50
bird_pos_x = WIDTH // 4
bird_pos_y = HEIGHT // 2
bird_rect = pygame.Rect(
    bird_pos_x, bird_pos_y, bird_size, bird_size
    )

pipes = []
score = 0

script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, 'assets')

bird_assets = [
    pygame.image.load(os.path.join(assets_dir, 'bird1.png')).convert_alpha(),
    pygame.image.load(os.path.join(assets_dir, 'bird2.png')).convert_alpha(),
    pygame.image.load(os.path.join(assets_dir, 'bird3.png')).convert_alpha()
]
bird_img_index=0
bird_img = bird_assets[bird_img_index]
bird_animation_velocity = 0.1


GAME_OVER = False

try:
    font = pygame.font.SysFont('Arial', 40, bold=True)
except:
    font = pygame.font.Font(None, 40)

running = True
velocity_y = 0

def generate_new_pipes():
    new_pipe=Pipe(WIDTH+50)
    pipes.append(new_pipe)

def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

def bird_animation_sprite():
    global bird_img_index, SCREEN
    global bird_animation_velocity, bird_assets
    bird_img_index += bird_animation_velocity
    if bird_img_index >= len(bird_assets):
        bird_img_index = 0
    bird_img = bird_assets[int(bird_img_index)]
    bird_img = pygame.transform.scale(bird_img, (bird_size, bird_size))
    bird_img.set_colorkey(WHITE)
    bird_img = pygame.transform.flip(bird_img, True, False)

    SCREEN.blit(bird_img, bird_rect)

generate_new_pipes()

last_pipe_time = pygame.time.get_ticks()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN and not GAME_OVER:
            if event.key == pygame.K_SPACE:
                velocity_y = VELOCITY

    if not GAME_OVER:

        velocity_y += GRAVITY

        if velocity_y >10:
            velocity_y = 10
        
        bird_rect.y += velocity_y

        if bird_rect.bottom >= HEIGHT:
            bird_rect.bottom = HEIGHT
            GAME_OVER = True

        elif bird_rect.top <= 0:
            bird_rect.top = 0
            GAME_OVER = True

        current_time = pygame.time.get_ticks()
        
        if current_time - last_pipe_time > 2500:
            generate_new_pipes()
            last_pipe_time = current_time

        
        SCREEN.fill(BLUE_SKY)
        bird_animation_sprite()


        for pipe in pipes:
            pipe.move()
            pipe.draw(SCREEN)
            if pipe.check_collision(bird_rect):
                GAME_OVER = True

            if pipe.pos_x + pipe.width < bird_rect.x and not pipe.passed:
                score += 1
                pipe.passed = True

        show_score()

        for pipe in pipes:
            if pipe.pos_x + pipe.width < 0:
                pipes.remove(pipe)

        if GAME_OVER:
            game_over_text = font.render("Game Over", True, BLACK)
            SCREEN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
            


        pygame.display.flip()

        CLOCK.tick(FPS)

pygame.quit()
quit()