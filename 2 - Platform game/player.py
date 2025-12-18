import pygame
from Physics.physics import PhysicsEngine


class Player(PhysicsEngine): #TODO: Refactor this class
    def __init__(self, x, y, game_screen):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.max_speed = 5
        self.jump_force = -20
        self.maximum_fall_speed = 10
        self.health = 3
        self.knockback_force = 10
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 0, 0)

        # Horizontal movement
        self.dx = 0 
        self.acceleration_rate = 10
        self.friction = 30


        # Vertical movement
        self.vy = 0
        self.gravity = 60
        self.on_ground = False
        self.is_holding_jump = False
        self.variable_jump_multiplier = -18 # Reduces upward velocity when jump is held

        # Advanced jump mechanics
        self.COYOTE_DURATION = 0.15
        self.coyote_time = 0
        self.BUFFER_JUMP_DURATION = 0.15
        self.buffer_jump = 0

        # State
        self.wants_to_jump = False
        self.move_direction = 0 # -1 for left, 1 for right, 0 for idle

        # Game info
        self.coins_collected = 0
        self.screen_width = game_screen
        
    def draw(self, surface, offset_x=0):
        draw_rect = self.rect.copy()
        draw_rect.x -= offset_x
        pygame.draw.rect(surface, self.color, draw_rect)

    def _handle_input(self):
        keys = pygame.key.get_pressed()
        
        self.move_direction = 0
        if keys[pygame.K_LEFT]:
            self.move_direction = -1
        elif keys[pygame.K_RIGHT]:
            self.move_direction = 1

        self.wants_to_jump = keys[pygame.K_SPACE] or keys[pygame.K_UP]
        if self.wants_to_jump:
            self.buffer_jump = self.BUFFER_JUMP_DURATION

        self.is_holding_jump = self.wants_to_jump

    def _update_timers(self, delta_time):
        if not self.on_ground:
            self.coyote_time -= delta_time
        
        if self.buffer_jump > 0:
            self.buffer_jump -= delta_time

    def _apply_horizontal_movement(self, delta_time, offset_x):
        if self.move_direction != 0:
            self.dx += (self.acceleration_rate * self.move_direction * delta_time)
        else: # Apply friction
            if self.dx > 0:
                self.dx -= self.friction * delta_time
                if self.dx < 0: self.dx = 0
            elif self.dx < 0:
                self.dx += self.friction * delta_time
                if self.dx > 0: self.dx = 0

        self.dx = max(-self.max_speed, min(self.max_speed, self.dx))

    def _apply_vertical_movement(self, delta_time):
        # Jump logic
        if self.buffer_jump > 0 and (self.on_ground or self.coyote_time > 0):
            self.vy = self.jump_force
            self.on_ground = False
            self.coyote_time = 0
            self.buffer_jump = 0
        
        # Variable jump height
        if self.is_holding_jump and self.vy < 0:
            self.vy += self.variable_jump_multiplier * delta_time

        # Gravity
        self.vy += self.gravity * delta_time
        self.vy = min(self.vy, self.maximum_fall_speed)

    def handle_horizontal_collisions(self, other_rects):
        self.rect.x += self.dx
        for rect in other_rects:
            if self.rect.colliderect(rect):
                if self.dx > 0:
                    self.rect.right = rect.left
                elif self.dx < 0:
                    self.rect.left = rect.right
                self.dx = 0

    def handle_vertical_collisions(self, other_rects):
        self.rect.y += self.vy
        self.on_ground = False
        for platform in other_rects:
            if self.rect.colliderect(platform):
                if self.vy > 0: # Moving down
                    self.rect.bottom = platform.top
                    self.on_ground = True
                    self.coyote_time = self.COYOTE_DURATION
                elif self.vy < 0: # Moving up
                    self.rect.top = platform.bottom
                self.vy = 0

    def _enforce_screen_boundaries(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
            self.dx = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.dx = 0

    def update(self, other_rects, **kwargs):
        delta_time = kwargs.get("delta_time")
        if delta_time is None: delta_time = 1/60.0

        self._handle_input()
        self._update_timers(delta_time)
        self._apply_horizontal_movement(delta_time, kwargs.get("offset_x", 0))
        self._apply_vertical_movement(delta_time)
        
        self.handle_horizontal_collisions(other_rects)
        self.handle_vertical_collisions(other_rects)
        self._enforce_screen_boundaries()

    def knock_back_hit(self):
        self.vx = self.move_direction * self.knockback_force
        self.vy = -self.knockback_force
        
    def update_collected_coins(self, qty):
        self.coins_collected += qty
       

        