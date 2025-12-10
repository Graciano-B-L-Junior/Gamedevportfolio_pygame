import pygame

class Player:
    def __init__(self, x, y, game_screen):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 100
        self.jump_force = -20
        self.maximum_fall_speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        self.color = (255, 0, 0)
        self.dx = 0 
        self.acceleration_rate = 15
        self.friction = 30 
        self.y_velocity = 0
        self.gravity = 60
        self.on_ground = False
        self.is_jumping = False
        self.high_jump = -18
        self.COYOTE_DURATION = 0.15
        self.coyote_time = 0
        self.is_colliding = False
        self.buffer_jump = 0
        self.BUFFER_JUMP_DURATION = 0.15

        self.screen_width = game_screen
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, other_rects, **kwargs):
        self.is_colliding = False
        keys = pygame.key.get_pressed()
        delta_time = kwargs.get("delta_time")
        if delta_time is None: delta_time = 1/60.0
 
        if not self.on_ground:
            self.coyote_time -= delta_time
        
        if self.buffer_jump > 0:
            self.buffer_jump -= delta_time

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.buffer_jump = self.BUFFER_JUMP_DURATION
        

        # Condição de pulo normal (e com coyote time)
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and (self.on_ground or self.coyote_time > 0):
            self.y_velocity = self.jump_force
            self.on_ground = False
            self.is_jumping = True
            self.coyote_time = 0
        
        if self.is_jumping:
            self.y_velocity += self.high_jump * delta_time
        else:
            self.is_jumping = False

        if kwargs.get("cam_offset_x") and kwargs.get('cam_is_moving'):
            self.speed = 180
        else:
            self.speed = 300

        if keys[pygame.K_LEFT]:
            self.dx -= self.acceleration_rate * delta_time
        elif keys[pygame.K_RIGHT]:
            self.dx += self.acceleration_rate * delta_time
        else:
            if self.dx > 0:
                self.dx -= self.friction * delta_time
                if self.dx < 0: self.dx = 0
            elif self.dx < 0:
                self.dx += self.friction * delta_time
                if self.dx > 0: self.dx = 0

        if self.dx > self.speed:
            self.dx = self.speed
        if self.dx < -self.speed:
            self.dx = -self.speed

        
        self.old_x = self.rect.x
        self.rect.x += self.dx
        for platform in other_rects:
            platform = platform[0]
            if self.rect.colliderect(platform):
                mtv_x = self.get_mtv_x(platform, self.dx)
                
                if self.dx > 0:
                    self.rect.right += mtv_x
                elif self.dx < 0:
                    self.rect.left += mtv_x
                self.dx = 0
                self.is_colliding=True

        self.y_velocity += self.gravity * delta_time
        self.y_velocity = min(self.y_velocity, self.maximum_fall_speed)

        self.old_y = self.rect.y
        self.rect.y += self.y_velocity
        self.on_ground = False
        for platform in other_rects:
            platform = platform[0]
            if self.rect.colliderect(platform):
                if self.y_velocity > 0:
                    self.rect.y = self.old_y
                    self.y_velocity = 0
                    self.on_ground = True
                    self.coyote_time = self.COYOTE_DURATION
                    # Verifica se o pulo foi "bufferizado"
                    if self.buffer_jump > 0:
                        self.y_velocity = self.jump_force
                        self.on_ground = False
                        self.is_jumping = True
                        self.coyote_time = 0
                        self.buffer_jump = 0 # Consome o buffer
                elif self.y_velocity < 0:
                    self.rect.y = self.old_y
                    self.y_velocity = 0
                self.is_colliding=True
        

        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
            self.dx = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.dx = 0

    def get_mtv_x(self, rect, move_x):
        overlap_right = self.rect.right - rect.left
        overlap_left = rect.right - self.rect.left

        if move_x > 0 and self.rect.right > rect.left:
            return -overlap_right
        elif move_x < 0 and self.rect.left < rect.right:
            return overlap_left
        else:
            return 0

        