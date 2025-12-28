import pygame

class PhysicsEngine:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 50  # Initial horizontal velocity for enemy movement
        self.vy = 0
        self.gravity = 100
        self.other_rects = []
        self.on_ground = False

    def update(self, delta_time):
        # Horizontal Movement
        self.x += self.vx * delta_time
        self.rect.x = round(self.x)
        self.handle_horizontal_collisions()

        # Vertical Movement
        self.vy += self.gravity * delta_time
        self.y += self.vy * delta_time
        self.rect.y = round(self.y)
        self.handle_vertical_collisions()

        # Update internal position from rect after collision resolution
        self.x = self.rect.x
        self.y = self.rect.y

        self.check_ledge()

    def handle_horizontal_collisions(self):
        for other in self.other_rects:
            if self.rect.colliderect(other):
                if self.vx > 0:
                    self.rect.right = other.left
                elif self.vx < 0:
                    self.rect.left = other.right
                self.vx *= -1
                self.x = self.rect.x 
                break

    def handle_vertical_collisions(self):
        self.on_ground = False
        for other in self.other_rects:
            if self.rect.colliderect(other):
                if self.vy > 0:  
                    self.rect.bottom = other.top
                    self.on_ground = True
                    self.vy = 0
                elif self.vy < 0:
                    self.rect.top = other.bottom
                    self.vy = 0
                self.y = self.rect.y

    def check_ledge(self):
        """Checks if the enemy is at a ledge and turns around if so."""
        if not self.on_ground:
            return

        # Create a small rect just below the enemy's front foot
        probe_x = self.rect.right if self.vx > 0 else self.rect.left - 1
        probe_rect = pygame.Rect(probe_x, self.rect.bottom, 1, 1)

        is_ground_ahead = False
        for platform in self.other_rects:
            if probe_rect.colliderect(platform):
                is_ground_ahead = True
                break

        if not is_ground_ahead:
            self.vx *= -1

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
