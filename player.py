from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_clock = 0
        

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.wrap_around_move()
        self.shot_clock -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.impulse_prograde(dt)
        if keys[pygame.K_s]:
            self.impulse_prograde(dt*-PLAYER_REVERSE_SPEED_MODIFIER)
        if keys[pygame.K_x]:
            self.impulse_retrograde(dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.move()
    
    def move(self):
        self.position += self.velocity

    def impulse_prograde(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        movement = forward * PLAYER_SPEED * dt
        self.velocity += movement

    def impulse_retrograde(self, dt):
        self.velocity += self.velocity * -1 * dt * PLAYER_RETROGRADE_SPEED

    def shoot(self, dt):
        if self.shot_clock <= 0:
            self.shot_clock = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED * dt + self.velocity

        

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.clock = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.clock += dt
        self.expired = self.clock > SHOT_TIME_TO_LIVE or self.wrap_count >= 1
        self.wrap_around_move()
        self.position += self.velocity