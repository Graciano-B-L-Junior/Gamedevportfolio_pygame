
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
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time

        for rect in self.other_rects:
            self.collision(rect)


    def collision(self, other):
        if self.vx > 0:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                self.rect.right = other.rect.left
                self.vx = 0
        elif self.vx < 0:
            if self.rect.left < other.rect.right and self.rect.right > other.rect.left:
                self.rect.left = other.rect.right
                self.vx = 0

        if self.vy > 0:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.rect.bottom = other.rect.top
                self.vy = 0
        elif self.vy < 0:
            if self.rect.top < other.rect.bottom and self.rect.bottom > other.rect.top:
                self.rect.top = other.rect.bottom
                self.vy = 0
    

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
